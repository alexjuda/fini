import argparse


def _run_edit():
    from .edit import main

    main()


def _run_rollover():
    from .rollover import main

    main()


def _run_sync():
    print("Nothing here for now.")


def _run_implicit():
    print("[rollover]")
    _run_rollover()

    print("[edit]")
    _run_edit()

    print("[sync]")
    _run_sync()


def _parser():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")
    _ = subparser.add_parser("edit")
    _ = subparser.add_parser("rollover")
    _ = subparser.add_parser("sync")

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

        case _:
            _run_implicit()
