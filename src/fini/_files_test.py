from pathlib import Path
import pytest
import re
from datetime import date
from freezegun import freeze_time
from ._files import TodoFile, today_todo_path, prev_day_todo


class TestTodayTodo:
    @staticmethod
    def test_path_looks_legit(monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("FINI_DIR", "/home/alex/Documents/todos")

        file_path = today_todo_path()

        assert (
            re.match(
                r"/home/alex/Documents/todos/\d{4}-\d{2}-\d{2}.md",
                str(file_path.absolute()),
            )
            is not None
        )


DAY_BEFORE_YESTERDAY = date.fromisoformat("2025-02-01")
YESTERDAY = date.fromisoformat("2025-02-02")
TODAY = date.fromisoformat("2025-02-03")


class TestPrevDateTodo:
    @staticmethod
    @pytest.fixture
    def fini_dir(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
        dir = tmp_path / "fini_dir"
        dir.mkdir()
        monkeypatch.setenv("FINI_DIR", str(dir))
        return dir

    @staticmethod
    def test_no_files(fini_dir):
        file = prev_day_todo()

        assert file is None

    @staticmethod
    @freeze_time(TODAY)
    def test_today_only(fini_dir: Path):
        for day in [TODAY]:
            (fini_dir / day.isoformat()).with_suffix(".md").touch()

        file = prev_day_todo()

        assert file is None

    @staticmethod
    @freeze_time(TODAY)
    def test_no_today(fini_dir: Path):
        for day in [YESTERDAY, DAY_BEFORE_YESTERDAY]:
            (fini_dir / day.isoformat()).with_suffix(".md").touch()

        file = prev_day_todo()

        assert file is not None
        assert file.date_ == YESTERDAY

    @staticmethod
    @freeze_time(TODAY)
    def test_multiple_files(fini_dir: Path):
        for day in [TODAY, YESTERDAY, DAY_BEFORE_YESTERDAY]:
            (fini_dir / day.isoformat()).with_suffix(".md").touch()

        file = prev_day_todo()

        assert file is not None
        assert file.date_ == YESTERDAY

    @staticmethod
    def test_not_matching_filenames(fini_dir: Path):
        (fini_dir / "foo_bar.txt").touch()

        file = prev_day_todo()

        assert file is None


class TestTodoFile:
    class TestParsePath:
        @staticmethod
        def test_valid():
            path = Path("notes/2025-01-02.md")

            file = TodoFile.parse_path(path)

            assert file is not None
            assert file.path.suffix == ".md"
            assert file.date_ == date(2025, 1, 2)

        @staticmethod
        def test_no_date():
            path = Path("notes/foo.md")

            file = TodoFile.parse_path(path)

            assert file is None

        @staticmethod
        def test_date_with_things():
            path = Path("notes/foo-2025-03-04-bar.md")

            file = TodoFile.parse_path(path)

            assert file is None
