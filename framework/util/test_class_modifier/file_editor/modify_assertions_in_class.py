import sys
from os import path


def modify(readable_file_path):
    global file_path
    file_path = readable_file_path
    read_file()
    replace_newline_from_assertions()
    store_file()


def read_file():
    global file_contents
    if not path.exists(file_path):
        print("File not exist!")
        sys.exit(2)
    f = open(file_path)
    file_contents = f.read().splitlines()
    f.close()


def replace_newline_from_assertions():
    global file_contents
    file_str = ''
    assert_started = False
    for idx, line in enumerate(file_contents):
        if line.__contains__("assert") and line.__contains__(";"):
            file_str = file_str + line + '\n \n'
        elif line.__contains__("assert") and not line.__contains__(";"):
            file_str = file_str + line
            assert_started = True
        elif assert_started and line.__contains__(";"):
            file_str = file_str + line + '\n \n'
            assert_started = False
        elif assert_started and not line.__contains__(";"):
            file_str = file_str + line
        else:
            file_str = file_str + line + '\n'

    file_contents = file_str


def store_file():
    global file_contents
    f = open(file_path, 'w')
    f.write("".join(file_contents))
    f.write("\n")
    f.close()