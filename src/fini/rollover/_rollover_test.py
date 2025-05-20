from pathlib import Path

from pytest import fixture
from ._rollover import rollover_file


class TestRolloverFile:
    @fixture
    @staticmethod
    def file_in(tmp_path: Path) -> Path:
        return tmp_path / "in.md"

    @fixture
    @staticmethod
    def file_out(tmp_path: Path) -> Path:
        return tmp_path / "out.md"

    @staticmethod
    def test_simplest(file_in: Path, file_out: Path):
        file_in.write_text("* [ ] hello\n")

        rollover_file(file_in, file_out)

        assert file_out.read_text() == "* [ ] hello\n"
