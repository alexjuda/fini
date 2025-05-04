import subprocess
from .._config import editor
from .._files import today_todo_path


def main():
    cmd = [editor(), str(today_todo_path())]
    print(f"Launching $({' '.join(cmd)})")
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        raise ValueError(f"Running '{cmd}' failed with code {proc.returncode}")
