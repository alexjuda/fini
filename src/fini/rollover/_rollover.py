import re
from pathlib import Path

from .._files import prev_day_todo, today_todo_path


DONE_TASK_PATTERN = re.compile(r"^\s*([-\*]) +\[x]")
INDENT_PATTERN = re.compile(r"^\s*(\S)")


def line_indent(line: str) -> int:
    match = INDENT_PATTERN.match(line)
    if not match:
        return 0
    return match.start(1)


def _drop_done(prev_path: Path, new_path: Path):
    with prev_path.open() as f_in, new_path.open("w") as f_out:
        done_section_indent = None
        for line in f_in:
            current_indent = line_indent(line)

            if done_section_indent is not None:
                if done_section_indent < current_indent:
                    continue
                else:
                    # We're past the section.
                    done_section_indent = None

            match = DONE_TASK_PATTERN.match(line)
            # Find out the indentation of the section we want to remove.
            if (
                # When the first line matches '* [x]'
                match
                # When we aren't already in a nested section.
                and not done_section_indent
            ):
                done_section_indent = match.start(1)

            if not match:
                f_out.write(line)


def _drop_multi_empty_lines(path: Path):
    text = path.read_text()
    fixed_text = re.sub(r"\n\n+", "\n\n", text)
    path.write_text(fixed_text)


def rollover_file(prev_path: Path, new_path: Path):
    _drop_done(prev_path, new_path)
    _drop_multi_empty_lines(new_path)


def main():
    todo_path = today_todo_path()

    if todo_path.exists():
        print(f"Skipping. Todo file for today already exists: {todo_path}")
        return

    if not (prev_todo := prev_day_todo()):
        raise ValueError("No prev day todo file found")

    rollover_file(prev_todo.path, todo_path)
    print(f"Rolled over {prev_todo.path.name} to {todo_path.name}")
