#!/usr/bin/env python
import argparse

from loadRollTables import load_roll_tables
from selectLootbox import user_interaction


def main(args):
    load_roll_tables()
    user_interaction(args.quickroll, args.manual)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A DM tool used for rolling lootboxes of verying qualities",
        epilog="As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
        fromfile_prefix_chars='@')
    # TODO Specify your real parameters here.
    parser.add_argument(
        "-qr",
        "--quickroll",
        type=str,
        help="select an option and bypass the prompt",
        default=None,
        metavar="ARG")
    parser.add_argument(
        "-m",
        "--manual",
        help="manually input rolls instead of using an auto-roller",
        action="store_true")
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    args = parser.parse_args()

    main(args)
