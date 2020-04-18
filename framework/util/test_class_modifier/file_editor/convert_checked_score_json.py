import json
import os.path


def read_format_file(file_path):
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
            current_dict[method_name] = method_coverage_numbers
        if current_dict.__len__() > 0:
            final_output[class_value] = current_dict

    with open(file_path, 'w') as fp:
        json.dump(final_output, fp)
