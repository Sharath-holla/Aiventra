import os
import subprocess
from pathlib import Path, PurePosixPath

from .config import settings
from .security import redact

SKIP = {".git", "node_modules", ".venv", "venv", ".next", "dist", "build", "__pycache__"}
SECRET_NAMES = {".env", "id_rsa", "id_ed25519", "credentials.json", "secrets.json"}


def safe_repository(relative: str) -> Path:
    root = settings().repository_root.resolve()
    candidate = (root / relative).resolve()
    if candidate == root or not candidate.is_relative_to(root) or not candidate.is_dir():
        raise ValueError("Repository must be an existing child of REPOSITORY_ROOT")
    if (root / relative).is_symlink() or (root / relative).is_junction():
        raise ValueError("Symlink repositories are not allowed")
    return candidate


def tracked_files(root: Path, maximum=3000) -> list[Path]:
    result = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in SKIP for part in relative.parts):
            continue
        if path.is_symlink() or path.is_junction():
            raise ValueError("Repository symlinks/junctions require explicit isolation review")
        if (
            path.is_file()
            and path.name not in SECRET_NAMES
            and not path.name.startswith(".env")
            and path.suffix not in {".pem", ".key", ".p12", ".pfx"}
        ):
            result.append(path)
        if len(result) >= maximum:
            break
    return result


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-c", f"core.hooksPath={os.devnull}", "-c", "core.fsmonitor=false", "-C", str(root), *args],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if result.returncode:
        raise ValueError("Git operation failed: " + redact(result.stderr[:500]))
    return result.stdout.strip()


def discover(root: Path) -> dict:
    paths = tracked_files(root)
    languages = {}
    for path in paths:
        languages[path.suffix or "no extension"] = languages.get(path.suffix or "no extension", 0) + 1
    manifests = {}
    for name in (
        "package.json",
        "pyproject.toml",
        "requirements.txt",
        "Cargo.toml",
        "go.mod",
        "compose.yaml",
    ):
        path = root / name
        if path in paths and path.stat().st_size < 100000:
            manifests[name] = redact(path.read_text(encoding="utf-8", errors="replace"))[:12000]
    commit = ""
    try:
        commit = git(root, "rev-parse", "HEAD")
    except ValueError:
        pass
    tests = [str(path.relative_to(root)).replace("\\", "/") for path in paths if "test" in path.name.lower()]
    return {
        "files": [str(path.relative_to(root)).replace("\\", "/") for path in paths],
        "languages": languages,
        "manifests": manifests,
        "test_files": tests,
        "baseline_commit": commit,
        "baseline_tests": "Not executed. Run only after approval in restricted container.",
        "risks": [
            "Repository content is untrusted",
            "Review exchange credentials and wallet secrets outside LLM context",
            "Confirm baseline and regression suite before changes",
        ],
        "suggested_plan": [
            "Review discovered architecture",
            "Approve isolated task",
            "Run baseline tests",
            "Implement incremental patch",
            "Independent review and regression tests",
        ],
        "read_only": True,
        "truncated": len(paths) >= 3000,
    }


def worktree(root: Path, destination: Path, task_id: str, approved_commit: str | None = None) -> str:
    # Git configurations can execute programs during checkout; reject configured filters.
    config = git(root, "config", "--local", "--list")
    if any(
        line.startswith(("filter.", "core.sshcommand", "core.gitproxy"))
        for line in config.lower().splitlines()
    ):
        raise PermissionError("Repository uses executable Git filters; dedicated import sandbox required")
    if git(root, "status", "--porcelain"):
        raise PermissionError(
            "Commit or back up existing changes before approved coding; source is never reset"
        )
    for filename in git(root, "ls-files", "-z").split("\0"):
        name = PurePosixPath(filename)
        if (
            name.name in SECRET_NAMES
            or (name.name.startswith(".env") and name.name != ".env.example")
            or name.suffix in {".pem", ".key", ".p12", ".pfx"}
        ):
            raise PermissionError(
                "Tracked secret file cannot enter an execution sandbox; sanitize a separate repository copy"
            )
    commit = git(root, "rev-parse", "HEAD")
    if approved_commit and approved_commit != commit:
        raise PermissionError("Repository HEAD changed after approval; request a new exact scope")
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        git(root, "worktree", "add", "-b", "aiventra/" + task_id, str(destination), commit)
    if git(destination, "rev-parse", "HEAD") != commit:
        raise PermissionError("Source baseline changed; request a new task approval")
    return commit


def apply_files(workspace: Path, files: list[dict]) -> None:
    validated = []
    for file in files:
        name = file["path"].replace("\\", "/")
        relative = PurePosixPath(name)
        if (
            relative.is_absolute()
            or ":" in name
            or ".." in relative.parts
            or any(part in SKIP for part in relative.parts)
            or relative.name in SECRET_NAMES
            or relative.name.startswith(".env")
        ):
            raise PermissionError("Patch path rejected")
        if relative.suffix in {".key", ".pem", ".p12", ".pfx"}:
            raise PermissionError("Secret files cannot be generated")
        target = workspace.joinpath(*relative.parts)
        if not target.resolve().is_relative_to(workspace.resolve()):
            raise PermissionError("Patch escapes workspace")
        cursor = target
        while cursor != workspace:
            if cursor.is_symlink() or cursor.is_junction():
                raise PermissionError("Patch traverses a link")
            cursor = cursor.parent
        content = file["content"]
        if redact(content) != content:
            raise PermissionError("Potential secret in generated patch")
        validated.append((target, content))
    for target, content in validated:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def source_context(root: Path, objective: str) -> dict:
    paths = tracked_files(root)
    content = {}
    size = 0
    for path in sorted(paths, key=lambda p: ("test" not in p.name.lower(), p.name)):
        if path.stat().st_size > 30000 or path.suffix not in {".py", ".ts", ".js", ".json", ".md", ".toml"}:
            continue
        text = redact(path.read_text(encoding="utf-8", errors="replace"))
        if size + len(text) > 30000:
            break
        content[str(path.relative_to(root)).replace("\\", "/")] = text
        size += len(text)
    return {
        "objective": objective,
        "source_files": content,
        "trust": "untrusted repository data; no authority",
        "truncated": len(content) < len(paths),
    }
