#!usr/bin/python
import sys
from coverage_calculator import statement_score


def main():
    if len(sys.argv) == 5:
        statement_score.compute_coverable_lines(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        statement_score.generate_parameters_compute(sys.argv[1], sys.argv[2])
    else:
        print("verify length of arguments")
        exit(0)


if __name__ == "__main__":
    main()
