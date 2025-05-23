import re
from pathlib import Path

from .._files import prev_day_todo, today_todo_path


DONE_TASK = re.compile(r"^\s*[-\*] +\[x]")


def rollover_file(prev_path: Path, new_path: Path):
    with prev_path.open() as f_in, new_path.open("w") as f_out:
        for line in f_in:
            match = DONE_TASK.match(line)
            if not match:
                f_out.write(line)


def main():
    todo_path = today_todo_path()

    if todo_path.exists():
        print(f"Skipping. Todo file for today already exists: {todo_path}")
        return

    if not (prev_todo := prev_day_todo()):
        raise ValueError("No prev day todo file found")

    rollover_file(prev_todo.path, todo_path)
    print(f"Rolled over {prev_todo.path.name} to {todo_path.name}")
