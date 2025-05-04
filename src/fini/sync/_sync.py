import itertools
from pathlib import Path
from .._files import fini_dir
import git


def _edited_files(repo: git.Repo):
    diff_index = repo.index.diff(None)
    untracked_files = repo.untracked_files

    paths = []
    for file_diff in itertools.chain(
        # Added
        diff_index.iter_change_type("A"),
        # C = copied
        diff_index.iter_change_type("C"),
        # Deleted
        diff_index.iter_change_type("D"),
        # Renamed
        diff_index.iter_change_type("R"),
        # Modified data
        diff_index.iter_change_type("M"),
        # Type paths changed
        diff_index.iter_change_type("T"),
    ):
        assert file_diff.b_rawpath is not None
        paths.append(Path(file_diff.b_rawpath.decode()))

    for untracked_file in untracked_files:
        paths.append(Path(untracked_file))

    return sorted(paths)


def _push(repo: git.Repo):
    """
    Extracted for mocking out in tests.
    """
    repo.remote().push()


def main():
    repo = git.Repo(fini_dir())
    if not repo.is_dirty(untracked_files=True):
        print("Skipping. No changes.")
        return

    paths = _edited_files(repo)
    names = [p.stem for p in paths]

    repo.git.add(all=True)
    repo.index.commit(f"(fini) Edited {', '.join(names)}")

    print("Committed changes.")

    _push(repo)

    print("Pushed.")
