import argparse

from src.const import STATUSES
from src.literals import (
    HELP_AUTHOR, HELP_DESCRIPTION, HELP_ID, HELP_MODES,
    HELP_STATUS, HELP_TITLE, HELP_YEAR
)


def get_parser(modes: dict[str:object]):
    """
    Auxiliary function that creates, configures and returns argument parser.
    """
    parser = argparse.ArgumentParser(description=HELP_DESCRIPTION)
    parser.add_argument('mode', choices=modes, help=HELP_MODES)
    parser.add_argument('-id', '--id', type=int, action='store', help=HELP_ID)
    parser.add_argument(
        '-t', '--title', type=str, action='store', help=HELP_TITLE
    )
    parser.add_argument(
        '-a', '--author', type=str, action='store', help=HELP_AUTHOR
    )
    parser.add_argument(
        '-y', '--year', type=int, action='store', help=HELP_YEAR
    )
    parser.add_argument(
        '-s',
        '--status',
        type=int,
        choices=STATUSES.keys(),
        action='store',
        help=HELP_STATUS
    )
    return parser
