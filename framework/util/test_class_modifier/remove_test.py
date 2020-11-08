#!usr/bin/python
import sys
from file_editor import comment_lines_of_test


def main():
    arguments = len(sys.argv) - 1
    if arguments != 2:
        print("please verify arguments, size mismatch")
        sys.exit(2)
    comment_lines_of_test.modify(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
