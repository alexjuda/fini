from .._files import today_todo_path, all_todo_files


def main():
    all_files = set(all_todo_files())
    prev_files = all_files.difference({today_todo_path})
