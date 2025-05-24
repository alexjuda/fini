from pathlib import Path

import pytest

from ._rollover import line_indent, rollover_file


TEST_DATA = Path(__file__).parent / "test_data"


class TestLineIndent:
    @staticmethod
    def test_sample():
        assert line_indent("    *") == 4

    @staticmethod
    def test_empty():
        assert line_indent("") == 0


class TestRolloverFile:
    @staticmethod
    @pytest.mark.parametrize(
        "test_name",
        [
            "one_todo",
            "some_done",
            "list_formats",
            "nested_lists",
            "multiline_paragraph",
            "empty_lines",
            "headers",
            "plain_text",
            "complex",
        ],
    )
    def test_predefined_file_pair(tmp_path: Path, test_name: str):
        file_in = TEST_DATA / test_name / "in.md"
        file_expected = TEST_DATA / test_name / "expected_out.md"
        file_out = tmp_path / "out.md"

        rollover_file(file_in, file_out)

        assert  file_out.read_text() == file_expected.read_text()
