import shutil
from .._files import today_todo_path, prev_day_todo


def main():
    todo_path = today_todo_path()

    if todo_path.exists():
        raise ValueError(f"Todo file for today already exists: {todo_path}")

    if not (prev_todo := prev_day_todo()):
        raise ValueError("No prev day todo file found")

    shutil.copy(prev_todo.path, todo_path)
    print(f"Copied {prev_todo.path.name} to {todo_path.name}")
