from .._files import fini_dir
import git


def main():
    repo = git.Repo(fini_dir())
    if not repo.is_dirty(untracked_files=True):
        print("Skipping. No changes.")
        return
