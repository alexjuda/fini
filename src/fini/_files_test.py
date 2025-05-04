import pytest
import re
from ._files import todo_file


class TestTodoFile:
    @staticmethod
    def test_path_looks_legit(monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("FINI_DIR", "/home/alex/Documents/todos")

        file_path = todo_file()

        assert (
            re.match(
                r"/home/alex/Documents/todos/\d{4}-\d{2}-\d{2}.md",
                str(file_path.absolute()),
            )
            is not None
        )
