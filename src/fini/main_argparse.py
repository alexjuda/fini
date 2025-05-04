import argparse


def _run_edit():
    from .edit import main

    main()


def _run_rollover():
    from .rollover import main

    main()


def _run_sync():
    from .sync import main

    main()


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
    _ = subparser.add_parser("edit", help="Opens a daily todo file in your $EDITOR.")
    _ = subparser.add_parser(
        "rollover",
        help="Finds the todo file from a previous day and copies over for today.",
    )
    _ = subparser.add_parser("sync", help="Makes a commit & pushes to origin.")

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
