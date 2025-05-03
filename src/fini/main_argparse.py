import argparse



def _run_edit():
    print("edit")

def _run_rollover():
    print("edit")

def _run_sync():
    print("sync")

def _parser():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")
    edit_parser = subparser.add_parser("edit")
    rollover_parser = subparser.add_parser("rollover")
    sync_parser = subparser.add_parser("sync")

    return parser


def app():
    args = _parser().parse_args()

    match args.command:
        case "edit":
            _run_edit()

        case "rollover":
            _run_rollover()

        case "sync":
            _run_sync()
