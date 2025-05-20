from pathlib import Path
from markdown_it import MarkdownIt
from mdformat.renderer import MDRenderer
from .._files import today_todo_path, prev_day_todo


def rollover_file(prev_path: Path, new_path: Path):
    md = MarkdownIt()
    tokens = md.parse(prev_path.read_text())

    renderer = MDRenderer()
    cleaned_text = renderer.render(tokens, options={}, env={})
    new_path.write_text(cleaned_text)


def main():
    todo_path = today_todo_path()

    if todo_path.exists():
        print(f"Skipping. Todo file for today already exists: {todo_path}")
        return

    if not (prev_todo := prev_day_todo()):
        raise ValueError("No prev day todo file found")

    rollover_file(prev_todo.path, todo_path)
    print(f"Rolled over {prev_todo.path.name} to {todo_path.name}")
