from .._files import todo_file, all_todo_files


def main():
    all_files = set(all_todo_files())
    prev_files = all_files.difference({todo_file})
