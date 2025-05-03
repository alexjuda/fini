from datetime import date, datetime, timezone
from pathlib import Path

from ._config import fini_dir


def _today_date() -> date:
    now = datetime.now(timezone.utc).astimezone()
    return now.date()


def todo_file() -> Path:
    dir = fini_dir()
    today = _today_date()
    return (dir / today.isoformat()).with_suffix(".md")


def all_todo_files() -> list[Path]:
    pass
