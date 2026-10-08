"""Create local secrets without displaying them or changing existing configuration."""

import secrets
from pathlib import Path

root = Path(__file__).resolve().parents[1]
env = root / ".env"
if not env.exists():
    template = (root / ".env.example").read_text(encoding="utf-8")
    template = template.replace("replace-with-at-least-32-random-characters", secrets.token_urlsafe(48))
    template = template.replace("replace-with-a-long-unique-password", secrets.token_urlsafe(24))
    template = template.replace("replace-with-a-database-password", secrets.token_urlsafe(32))
    env.write_text(template, encoding="utf-8")
    print("Created private .env. Read OWNER_EMAIL and OWNER_PASSWORD there to sign in.")
else:
    print("Existing .env preserved.")
    current = env.read_text(encoding="utf-8")
    if "DB_PASSWORD=" not in current:
        with env.open("a", encoding="utf-8") as output:
            output.write("\nDB_PASSWORD=" + secrets.token_urlsafe(32) + "\n")
(root / "data").mkdir(exist_ok=True)
