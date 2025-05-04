from dataclasses import dataclass
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


# def all_todo_files() -> list[Path]:
#     ...


# def _


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



def prev_day_todo_file() -> TodoFile | None:
    dir = fini_dir()
    todo_files = (
        file
        for path in dir.iterdir()
        if (file := TodoFile.parse_path(path))
    )

    today = _today_date()
    prev_files = (file for file in todo_files if file.date_ != today)
    yesterday_file = max(prev_files, key=lambda f: f.date_)

    return yesterday_file
