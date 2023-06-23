#!/usr/bin/env python
import argparse

from loadRollTables import load_roll_tables
from selectLootbox import select_lootbox


def main(args):
    load_roll_tables()
    select_lootbox()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A DM tool used for rolling lootboxes of verying qualities",
        epilog="As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
        fromfile_prefix_chars='@')
    # TODO Specify your real parameters here.
    # parser.add_argument(
    #                     "argument",
    #                     help = "pass ARG to the program",
    #                     metavar = "ARG")
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    args = parser.parse_args()

    main(args)
