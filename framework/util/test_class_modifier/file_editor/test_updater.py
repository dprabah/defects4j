import sys
from os import path
from pathlib import Path

from file_editor import utils


def update(readable_file_path):
    global file_path
    file_path = readable_file_path

    read_file()
    add_log_method()
    surround_with_try_catch()
    # store_file()


def surround_with_try_catch():
    current_block = []
    test_start_index = 0
    test_close_index = 0
    for idx, line in enumerate(file_contents):
        if line.strip().startswith("private void") or line.strip().startswith("public void"):
            may_be_block(test_start_index, test_close_index)
            test_start_index = idx
        if line.strip().__contains__("}"):
            test_close_index = idx
    may_be_block(test_start_index, test_close_index)


def may_be_block(start_index, end_index):
    print(start_index, end_index)


def read_file():
    global file_contents
    if not path.exists(file_path):
        print("File not exist!")
        sys.exit(2)
    f = open(file_path)
    file_contents = f.read().splitlines()
    f.close()


def add_log_method():
    global file_contents
    for idx, line in enumerate(file_contents):
        if line.startswith("public class "):
            file_contents = file_contents[0:idx+1] + utils.log_method_text() + file_contents[idx+1:]
        break


def store_file():
    f = open(file_path, 'w')
    f.write("\n".join(file_contents))


def get_method_block():
    pass