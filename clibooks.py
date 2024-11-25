from src.functions import MODE_TO_FUNCTION
from src.parser import get_parser


def main():
    """
    Main function that reads the command line input from user
    and calls the respective function.
    """
    parser = get_parser(MODE_TO_FUNCTION.keys())
    args = parser.parse_args()
    MODE_TO_FUNCTION[args.mode](args)


if __name__ == '__main__':
    main()
