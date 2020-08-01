#!usr/bin/python
import sys
from file_editor import modify_assertions_in_class


def main():
    arguments = len(sys.argv) - 1
    if arguments != 1:
        print("please verify arguments, size mismatch")
        sys.exit(2)
    modify_assertions_in_class.modify(sys.argv[1])


if __name__ == "__main__":
    main()
