import sys
from file_editor import test_updater_v2


def main():
    arguments = len(sys.argv) - 1
    if arguments != 1:
        print("please verify arguments, size mismatch")
        sys.exit(2)
    test_updater_v2.update(sys.argv[1])


if __name__ == "__main__":
    main()
