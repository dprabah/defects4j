#!usr/bin/python
import sys
from file_editor import convert_checked_score_json


def main():
    arguments = len(sys.argv) - 1
    if arguments != 1:
        print("please verify arguments, size mismatch")
        sys.exit(2)
    convert_checked_score_json.read_format_file(sys.argv[1])


if __name__ == "__main__":
    main()
