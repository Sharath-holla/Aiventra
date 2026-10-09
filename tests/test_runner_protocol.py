from pathlib import Path
from uuid import uuid4

import pytest
from company_os.config import settings
from company_os.runner_protocol import RunInput
from company_os.sandbox import connection, run_tests, snapshot
from pydantic import ValidationError


@pytest.mark.parametrize(
    "path",
    [
        "../escape",
        "/etc/x",
        "x\\y",
        "C:/x",
        ".git/config",
        "x/.env.local",
        "id_rsa",
        "x/key.pem",
        "x/./y",
        "x//y",
    ],
)
def test_closed_runner_snapshot_paths(path):
    with pytest.raises(ValidationError):
        RunInput(job_id=uuid4(), suite="python-unittest", files={path: "unsafe"})


def test_runner_rejects_arbitrary_command_image_env_and_oversized_snapshot():
    base = {"job_id": uuid4(), "suite": "python-unittest", "files": {"test_safe.py": "pass"}}
    for key in ("command", "image", "env", "mounts"):
        with pytest.raises(ValidationError):
            RunInput(**base, **{key: "untrusted"})
    with pytest.raises(ValidationError):
        RunInput(**{**base, "files": {"large.py": "x" * 1000001}})
    with pytest.raises(ValidationError):
        RunInput(**{**base, "files": {f"f{i}.py": "x" * 900000 for i in range(6)}})
    assert RunInput(**base).timeout == 120


async def test_worker_never_falls_back_to_host_execution(company, monkeypatch):
    monkeypatch.setattr(settings(), "execution_enabled", False)
    with pytest.raises(PermissionError, match="disabled"):
        await run_tests(Path("."), "python-unittest")
    monkeypatch.setattr(settings(), "runner_url", "http://untrusted.example:2375")
    monkeypatch.setattr(settings(), "runner_token", "test-runner-authentication-token-long")
    with pytest.raises(PermissionError, match="dedicated runner"):
        connection()


def test_snapshot_omits_secrets_rejects_binary_links_and_secret_content(company, monkeypatch):
    root = company["root"] / "snapshot"
    root.mkdir()
    (root / "safe.py").write_text("print('only the snapshot enters Docker')")
    (root / ".env").write_text("never exported")
    assert list(snapshot(root)) == ["safe.py"]
    (root / "binary.bin").write_bytes(b"\xff\x00")
    with pytest.raises(PermissionError, match="Binary"):
        snapshot(root)
    (root / "binary.bin").unlink()
    monkeypatch.setenv("SNAPSHOT_TEST_SECRET", "test-snapshot-redaction-private-value")
    (root / "safe.py").write_text("test-snapshot-redaction-private-value")
    with pytest.raises(PermissionError, match="Potential secret"):
        snapshot(root)
