import os
from datetime import date, datetime, timezone
from pathlib import Path

def fini_dir() -> Path:
    try:
        dir = Path(os.environ["FINI_DIR"])
    except KeyError as e:
        raise ValueError("FINI_DIR env variable not set") from e

    dir = dir.expanduser()

    # We could create the directory here if it doesn't exist. However, I think this will not be a common
    # case. I definitely need a git repo, which I probably don't want to create automatically (or do I?). I can revisit
    # this later.

    return dir
