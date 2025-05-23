import os
from pathlib import Path


def fini_dir() -> Path:
    dir_str = os.environ.get("FINI_DIR", "")
    if not dir_str:
        raise ValueError("FINI_DIR env variable not set")

    dir = Path(dir_str)
    dir = dir.expanduser()

    # We could create the directory here if it doesn't exist. However, I think this will not be a common
    # case. I definitely need a git repo, which I probably don't want to create automatically (or do I?). I can revisit
    # this later.

    return dir


def editor() -> str:
    try:
        editor = os.environ["EDITOR"]
    except KeyError as e:
        raise ValueError("EDITOR env variable not set") from e
    return editor
