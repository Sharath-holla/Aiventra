import asyncio
import shutil
from pathlib import Path

from .config import settings
from .db import uid
from .security import redact

SUITES = {
    "python-unittest": ("python:3.12-slim", ["python", "-I", "-m", "unittest", "discover", "-v"]),
    "node-test": ("node:22-slim", ["node", "--test"]),
}


async def run_tests(workspace: Path, suite: str, timeout=120) -> dict:
    if not settings().execution_enabled or not shutil.which("docker"):
        raise PermissionError("Docker execution is unavailable or EXECUTION_ENABLED=false")
    image, command = SUITES[suite]
    name = "company-qa-" + uid()
    args = [
        "docker",
        "run",
        "--rm",
        "--name",
        name,
        "--pull=never",
        "--network=none",
        "--cpus=1",
        "--memory=512m",
        "--pids-limit=128",
        "--read-only",
        "--cap-drop=ALL",
        "--security-opt=no-new-privileges",
        "--user=10001:10001",
        "--tmpfs=/tmp:rw,noexec,nosuid,size=64m",
        "--mount",
        f"type=bind,src={workspace.resolve()},dst=/workspace,readonly",
        "--workdir=/workspace",
        "--env",
        "PYTHONDONTWRITEBYTECODE=1",
        image,
        *command,
    ]
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )
    chunks = []
    length = 0

    async def collect():
        nonlocal length
        while True:
            chunk = await process.stdout.read(8192)
            if not chunk:
                break
            chunks.append(chunk)
            length += len(chunk)
            if length > 500000:
                raise TimeoutError("Test output exceeded limit")
        return await process.wait()

    try:
        code = await asyncio.wait_for(collect(), timeout=timeout)
    except TimeoutError:
        process.kill()
        await process.wait()
        cleanup = await asyncio.create_subprocess_exec(
            "docker", "rm", "-f", name, stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.DEVNULL
        )
        await asyncio.wait_for(cleanup.wait(), timeout=15)
        code = 124
    return {
        "command": command,
        "environment": image + "; no network; read-only; 1CPU; 512MiB",
        "exit_code": code,
        "logs": redact(b"".join(chunks)[:500000].decode(errors="replace")),
    }
