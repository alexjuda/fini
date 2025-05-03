import os
from datetime import date, datetime, timezone
from pathlib import Path
import subprocess
from .._config import fini_dir


def _today_date() -> date:
    now = datetime.now(timezone.utc).astimezone()
    return now.date()


def _todo_file() -> Path:
    dir = fini_dir()
    today = _today_date()
    return (dir / today.isoformat()).with_suffix(".md")


def _editor() -> str:
    try:
        editor = os.environ["EDITOR"]
    except KeyError as e:
        raise ValueError("EDITOR env variable not set") from e
    return editor


def main():
    cmd = [_editor(), _todo_file()]
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        raise ValueError(f"Running '{cmd}' failed with code {proc.returncode}")
