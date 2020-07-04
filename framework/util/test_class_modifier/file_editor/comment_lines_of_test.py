import sys
from os import path


def modify(readable_file_path, method_name_to_modify):
    global method_name
    global file_path
    method_name = method_name_to_modify
    file_path = readable_file_path
    read_file()
    comment_it_out()
    store_file()


def read_file():
    global file_contents
    if not path.exists(file_path):
        print("File not exist!")
        sys.exit(2)
    f = open(file_path)
    file_contents = f.read().splitlines()
    f.close()


def comment_it_out():
    global file_contents
    for idx, line in enumerate(file_contents):
        if line.__contains__(method_name + "("):
            if file_contents[idx].__contains__("@Test"):
                file_contents = file_contents[0:idx] + \
                    [file_contents[idx].replace("@Test", "/*@Test*/")] + \
                    file_contents[idx+1:]
                break

            if file_contents[idx - 1].__contains__("@Test"):
                file_contents = file_contents[0:idx-1] + ['/*@Test*/'] + file_contents[idx:]
                break

            start, end = get_open_close_brace(idx)
            file_contents = file_contents[0: start + 1] + file_contents[end:]


def get_open_close_brace(idx):
    end_index_found = False
    count_braces = -1
    open_brace_index = 0
    close_brace_index = 0
    while not end_index_found:
        if not file_contents[idx].strip().startswith("//") and \
                not file_contents[idx].strip().startswith("*") and \
                file_contents[idx].__contains__("{"):

            if count_braces == -1:
                count_braces = 0
            count_braces = count_braces + 1
            if count_braces == 1:
                open_brace_index = idx
        if not file_contents[idx].strip().startswith("//") and \
                not file_contents[idx].strip().startswith("*") and \
                file_contents[idx].__contains__("}"):
            count_braces = count_braces - 1
            if count_braces == 0:
                close_brace_index = idx
        if count_braces == 0:
            end_index_found = True
        idx = idx + 1

    return open_brace_index, close_brace_index


def store_file():
    global file_contents
    f = open(file_path, 'w')
    f.write("\n".join(file_contents))
    f.write("\n")
    f.close()
