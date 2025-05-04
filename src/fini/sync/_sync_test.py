from pathlib import Path
from unittest.mock import Mock
import pytest
import git
from ._sync import main
from . import _sync


class TestMain:
    @pytest.fixture
    @staticmethod
    def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        fini_dir = tmp_path / "fini"
        fini_dir.mkdir()

        monkeypatch.setenv("FINI_DIR", str(fini_dir))

        repo = git.Repo.init(fini_dir)
        repo.index.commit("Initial")

        monkeypatch.setattr(_sync, "_push", Mock())

        return repo

    @staticmethod
    def test_edited_todo(repo: git.Repo, capsys: pytest.CaptureFixture):
        # Given
        todo_path = Path(repo.working_dir) / "2025-01-02.md"
        todo_path.write_text("Hello!")
        repo.git.add(all=True)
        repo.index.commit("Added test file")

        todo_path.write_text("Hello, there!")
        entry_before = repo.head.log_entry(-1)

        # When
        main()

        # Then
        outerr = capsys.readouterr()
        assert "Committed" in outerr.out
        assert "Pushed" in outerr.out

        entry_after = repo.head.log_entry(-1)
        assert entry_after != entry_before
        assert entry_after.message == "(fini) Edited 2025-01-02"

    @staticmethod
    def test_edited_two_todos(repo: git.Repo, capsys: pytest.CaptureFixture):
        # Given
        todo_path1 = Path(repo.working_dir) / "2025-01-01.md"
        todo_path2 = Path(repo.working_dir) / "2025-01-02.md"
        todo_path1.write_text("Hello!")
        todo_path2.write_text("Hello!")
        repo.git.add(all=True)
        repo.index.commit("Added test files")

        todo_path1.write_text("Hello, there!")
        todo_path2.write_text("Hello, there!")
        entry_before = repo.head.log_entry(-1)

        # When
        main()

        # Then
        outerr = capsys.readouterr()
        assert "Committed" in outerr.out
        assert "Pushed" in outerr.out

        entry_after = repo.head.log_entry(-1)
        assert entry_after != entry_before
        assert entry_after.message == "(fini) Edited 2025-01-01, 2025-01-02"

    @staticmethod
    def test_added_todo_file(repo: git.Repo, capsys: pytest.CaptureFixture):
        # Given
        todo_path = Path(repo.working_dir) / "2025-01-02.md"
        todo_path.write_text("Hello!")
        entry_before = repo.head.log_entry(-1)

        # When
        main()

        # Then
        outerr = capsys.readouterr()
        assert "Committed" in outerr.out
        assert "Pushed" in outerr.out

        entry_after = repo.head.log_entry(-1)
        assert entry_after != entry_before
        assert entry_after.message == "(fini) Edited 2025-01-02"

    @staticmethod
    def test_no_changes(repo: git.Repo, capsys: pytest.CaptureFixture):
        main()

        outerr = capsys.readouterr()
        assert "Skipping" in outerr.out

    @staticmethod
    @pytest.mark.skip()
    def test_other_files_changed(repo: git.Repo):
        # Not sure what should be the behavior yet.
        ...
