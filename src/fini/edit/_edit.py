import os
from datetime import date, datetime, timezone
from pathlib import Path
import subprocess


def _fini_dir() -> Path:
    try:
        dir = Path(os.environ["FINI_DIR"])
    except KeyError as e:
        raise ValueError("FINI_DIR env variable not set") from e

    # We could create the directory here if it doesn't exist. However, I think this will not be a common
    # case. I definitely need a git repo, which I probably don't want to create automatically (or do I?). I can revisit
    # this later.

    return dir


def _today_date() -> date:
    now = datetime.now(timezone.utc).astimezone()
    return now.date()


def _todo_file() -> Path:
    dir = _fini_dir()
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
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        print(f"Running '{cmd}' failed with code {proc.returncode}. Stdout:")
        print(proc.stdout.decode())
        print("Stderr:")
        print(proc.stderr.decode())
