#!usr/bin/python
import sys
from file_editor import convert_checked_score_json


def main():
    arguments = len(sys.argv) - 1
    if arguments != 1:
        print("please verify arguments, size mismatch")
        sys.exit(2)
    folder_path = sys.argv[1].split("checked_coverage.json")[0]
    convert_checked_score_json.update_to_huge_file(folder_path, sys.argv[1])


if __name__ == "__main__":
    main()
