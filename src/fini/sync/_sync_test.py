from pathlib import Path
import pytest
import git
from ._sync import main


class TestMain:
    @pytest.fixture
    @staticmethod
    def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        fini_dir = tmp_path / "fini"
        fini_dir.mkdir()

        monkeypatch.setenv("FINI_DIR", str(fini_dir))

        repo = git.Repo.init(fini_dir)
        return repo


    @staticmethod
    def test_edited_todo(repo: git.Repo):
        ...

    @staticmethod
    def test_added_todo_file(repo: git.Repo):
        ...

    @staticmethod
    def test_no_changes(repo: git.Repo, capsys: pytest.CaptureFixture):
        main()

        outerr = capsys.readouterr()
        assert "Skipping" in outerr.out


    @staticmethod
    def test_other_files_changed(repo: git.Repo):
        ...
