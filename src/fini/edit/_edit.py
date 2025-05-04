import subprocess
from .._config import editor
from .._files import today_todo_path


def main():
    cmd = [editor(), today_todo_path()]
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        raise ValueError(f"Running '{cmd}' failed with code {proc.returncode}")
