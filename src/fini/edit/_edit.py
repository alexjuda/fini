from datetime import date, datetime, timezone
from pathlib import Path
import subprocess
from .._config import fini_dir, editor


def _today_date() -> date:
    now = datetime.now(timezone.utc).astimezone()
    return now.date()


def _todo_file() -> Path:
    dir = fini_dir()
    today = _today_date()
    return (dir / today.isoformat()).with_suffix(".md")


def main():
    cmd = [editor(), _todo_file()]
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        raise ValueError(f"Running '{cmd}' failed with code {proc.returncode}")
