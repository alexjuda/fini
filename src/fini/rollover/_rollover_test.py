from pathlib import Path

from ._rollover import rollover_file


TEST_DATA = Path(__file__).parent / "test_data"


class TestRolloverFile:
    @staticmethod
    def test_one_todo(tmp_path: Path):
        file_in = TEST_DATA / "one_todo" / "in.md"
        file_out = tmp_path / "out.md"
        file_expected = TEST_DATA / "one_todo" / "expected_out.md"

        rollover_file(file_in, file_out)

        assert file_expected.read_text() == "* [ ] hello\n"
