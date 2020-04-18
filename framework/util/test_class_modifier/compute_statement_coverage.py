#!usr/bin/python
import sys
from coverage_calculator import statement_score


def main():
    arguments = len(sys.argv) - 3
    if arguments != 1:
        print("please verify arguments, size mismatch")
        sys.exit(2)
    statement_score.compute(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
