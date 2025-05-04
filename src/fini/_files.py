from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

from ._config import fini_dir


def _today_date() -> date:
    now = datetime.now(timezone.utc).astimezone()
    return now.date()


@dataclass
class TodoFile:
    path: Path
    date_: date

    @classmethod
    def parse_path(cls, path: Path) -> "TodoFile | None":
        try:
            date_ = date.fromisoformat(path.stem)
        except ValueError:
            return None

        return cls(path=path, date_=date_)


def today_todo_path() -> Path:
    """
    Doesn't matter if the file exists.
    """
    dir = fini_dir()
    today = _today_date()
    return (dir / today.isoformat()).with_suffix(".md")


def prev_day_todo() -> TodoFile | None:
    """
    Returns `TodoFile` only if that file exists.
    """
    dir = fini_dir()
    todo_files = (file for path in dir.iterdir() if (file := TodoFile.parse_path(path)))

    today = _today_date()
    prev_files = (file for file in todo_files if file.date_ != today)
    try:
        yesterday_file = max(prev_files, key=lambda f: f.date_)
    except ValueError:
        # max() raises ValueError when the seq is empty.
        return None

    return yesterday_file
