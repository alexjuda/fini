import subprocess
from .._config import editor
from .._files import todo_file


def main():
    cmd = [editor(), todo_file()]
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        raise ValueError(f"Running '{cmd}' failed with code {proc.returncode}")
