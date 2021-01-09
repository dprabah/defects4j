import json
import os.path
from os import path


def read_json_file(file_path):
    if not path.exists(file_path):
        # print("File not exist!" + file_path)
        output = {}
    else:
        with open(file_path, encoding="ISO-8859-1") as fp:
            output = json.load(fp)

    for key in output:
        for slave in output[key]:
            output[key][slave] = sorted(list(set(output[key][slave])))
    return output


def read_format_file(file_path, to_save):
    output = {}
    final_output = {}
    if os.path.exists(file_path):
        with open(file_path) as fp:
            output = json.load(fp)

    for class_value in output:
        current_dict = {}
        content_to_modify = output[class_value]
        for method_coverage in content_to_modify.split("],"):
            if method_coverage.strip() == "":
                break
            method_name = method_coverage.strip().split("[")[0]
            method_coverage_numbers = method_coverage.strip().split("[")[1].split(",")
            current_dict[method_name] = list(map(int, method_coverage_numbers))
        if current_dict.__len__() > 0:
            final_output[class_value] = current_dict

    with open(to_save, 'w') as fp:
        json.dump(final_output, fp)


master_file = dict()


def remove_empty_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d


def update_to_huge_file(folder_path, to_save):
    global master_file
    for root, dirs, files in os.walk(os.path.abspath(folder_path)):
        for file in files:
            json_file = os.path.join(root, file)
            if json_file.endswith(".slice.output.result.json"):
                print("Computing for -> " + str(json_file))
                if master_file.__len__() == 0:
                    master_file = read_json_file(json_file)
                    continue
                compute(read_json_file(json_file))

    with open(to_save, 'w') as fp:
        json.dump(remove_empty_from_dict(master_file), fp)


def compute(json_file_to_append):
    for key in master_file:
        master_file[key].update(json_file_to_append[key])
