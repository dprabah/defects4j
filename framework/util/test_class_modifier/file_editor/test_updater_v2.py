import sys
from os import path
import re

from file_editor import utils


def update(readable_file_path):
    global log_necessary
    global file_path
    log_necessary = False
    file_path = readable_file_path
    # The steps has to follow in order, modifying may makes code changes weired!!
    read_file()  # Step 1.
    add_log_inside_catch_block()  # Step 2.
    surround_with_try_catch_log_exception()  # Step 3.
    add_log_method()  # Step 4. # We add log method only where ever necessary!
    store_file()  # Step 5.


def add_log_inside_catch_block():
    global log_necessary
    for idx, line in enumerate(file_contents):
        if line.__contains__("catch"):
            process_catch_line(idx)
            log_necessary = True


def surround_with_try_catch_log_exception():
    global log_necessary
    for idx, line in enumerate(file_contents):
        if line.__contains__("@Test(expected"):
            process_test_expected(idx)
            log_necessary = True


def process_test_expected(idx):
    start, end = get_open_close_brace(idx)
    current_line = file_contents[start]

    if current_line.__contains__("throws") or file_contents[start - 1].__contains__("throws"):
        line_idx = current_line.index("{") + 1
        current_line = current_line[0:line_idx] + "\n\ttry {" + current_line[line_idx:]
        file_contents[start] = current_line
    else:
        line_idx = current_line.index("{")
        current_line = current_line[0:line_idx] + " throws Exception { \n\ttry {" + current_line[line_idx+1:]
        file_contents[start] = current_line

    exception_signature = get_exception_signature(current_line)
    current_line = file_contents[end]
    line_idx = current_line.index("}") - 1
    current_line = current_line[0:line_idx] + "\t}catch(" +exception_signature+" e){\n\t\tlogException(e);\n\t\tthrow e;\n\t}\n" + current_line[line_idx:]
    file_contents[end] = current_line


def get_exception_signature(current_line):
    line_as_array = current_line.split(" ")
    exception_index = [i for i, phrase in enumerate(line_as_array) if phrase.__contains__("Exception")]
    return "Exception" if exception_index.__len__() == 0 else line_as_array[exception_index[-1]]


def get_open_close_brace(idx):
    end_index_found = False
    count_braces = -1
    open_brace_index = 0
    close_brace_index = 0
    while not end_index_found:
        idx = idx + 1
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

    return open_brace_index, close_brace_index


def process_catch_line(idx):
    current_line = file_contents[idx]
    if current_line.__contains__("Exception") and \
            not current_line.strip().startswith("//") and \
            not current_line.strip().startswith("*"):
        exception_var = get_exception_variable(current_line)
        if current_line.__contains__("{"):
            line_idx = current_line.rindex("{") + 1
        elif file_contents[idx + 1].__contains__("{"):
            idx = idx + 1
            current_line = file_contents[idx]
            line_idx = current_line.rindex("{") + 1
        else :
            return
        current_line = current_line[0:line_idx] \
                       + "\n \t\t\tlogException("+exception_var+");\n" \
                       + current_line[line_idx:]
        file_contents[idx] = current_line


def get_exception_variable(current_line):
    line_as_array = current_line.replace(" )", ")").replace(" )", ")").split("//")[0]

    res = max(idx for idx, val in enumerate(line_as_array.split(" "))
              if val.__contains__(')'))
    uncleaned_exception_var = line_as_array.split(" ")[res]
    exception_variable = " ".join(re.findall("[a-zA-Z]+", uncleaned_exception_var))
    return exception_variable


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
    if log_necessary:
        for idx, line in enumerate(file_contents):
            if line.startswith("public class ") or \
                    line.__contains__("abstract class") or \
                    line.startswith("public final class ") or\
                    line.startswith("public static final class "):
                idx_incrementer = 1
                while not line.__contains__("{"):
                    line = file_contents[idx + idx_incrementer]
                    idx_incrementer = idx_incrementer + 1

                file_contents = file_contents[0:idx+idx_incrementer] + utils.log_method_text() + file_contents[idx+idx_incrementer:]
                # if line.__contains__("{"):
                #     file_contents = file_contents[0:idx+1] + utils.log_method_text() + file_contents[idx+1:]
                #     break
                # else:
                #     file_contents = file_contents[0:idx + 2] + utils.log_method_text() + file_contents[idx + 2:]
                break


def store_file():
    global file_contents
    f = open(file_path, 'w')
    f.write("\n".join(file_contents))
    f.write("\n")
    f.close()


def get_method_block():
    pass
