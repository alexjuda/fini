import pytest
from ._config import fini_dir, editor


class TestFiniDir:
    @staticmethod
    def test_no_env_var(monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("FINI_DIR", "")

        with pytest.raises(ValueError):
            fini_dir()

    @staticmethod
    def test_with_env_var(monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("FINI_DIR", "/home/alex/foo")

        dir = fini_dir()

        assert dir is not None

    @staticmethod
    def test_expands_home(monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("FINI_DIR", "~/Documents/fini-notes")

        dir = fini_dir()

        assert dir.is_absolute()


class TestEditor:
    @staticmethod
    def test_no_env_var(monkeypatch: pytest.MonkeyPatch):
        # I often have it set during development
        monkeypatch.delenv("EDITOR")

        with pytest.raises(ValueError):
            editor()

    @staticmethod
    def test_with_env_var(monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("EDITOR", "nvim")

        ed = editor()

        assert ed is not None
