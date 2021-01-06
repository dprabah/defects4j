import os
from os import path
from xml.dom import minidom
import json
import re


def generate_parameters_compute(checked_code_root, json_store_path):
    for root, dirs, files in os.walk(os.path.abspath(checked_code_root)):
        for file in files:
            xml_file_path = os.path.join(root, file)
            if xml_file_path.__contains__("::") and xml_file_path.endswith("coverage.xml"):
                print("Computing for -> " + str(xml_file_path))
                compute(xml_file_path, json_store_path, xml_file_path.split("/")[-2])


def compute(xml_file_path, json_store_path, executed_method):
    xml_doc = minidom.parse(xml_file_path)
    classes = xml_doc.getElementsByTagName('class')
    readable_file_path = json_store_path + "/line_coverage.json"
    output = {}
    if path.exists(readable_file_path):
        with open(readable_file_path) as fp:
            output = json.load(fp)
    for current_class in classes:
        class_name = current_class.attributes['name'].value
        lines = current_class.getElementsByTagName('line')
        line_nr = []
        numbers = {}
        for line in lines:
            if int(line.attributes['hits'].value) > 0:
                line_nr.append(int(line.attributes['number'].value))
        if line_nr.__len__() > 0:
            numbers[executed_method] = sorted(list(set(line_nr)))
            try:
                output[class_name].update(numbers)
            except KeyError:
                output[class_name] = numbers

    with open(readable_file_path, 'w') as fp:
        json.dump(output, fp)


def compute_coverable_lines(xml_file_path, json_store_path, project_path, ignorable_strings=""):
        xml_doc = minidom.parse(xml_file_path)
        classes = xml_doc.getElementsByTagName('class')
        numbers = {}
        for current_class in classes:
            class_path = {}
            var_class_name = current_class.attributes['name'].value
            lines = current_class.getElementsByTagName('line')
            line_nr = []
            for line in lines:
                line_nr.append(int(line.attributes['number'].value))

            path_to_class = project_path + "/" + var_class_name.replace(".", "/") + ".java"
            class_path['statement_coverable_lines'] = sorted(list(set(line_nr)))
            class_path['checked_coverable_lines'] = \
                compute_checked_coverable_lines(
                    path_to_class, class_path['statement_coverable_lines'], ignorable_strings)
            numbers[var_class_name] = class_path

        with open(json_store_path + "/coverable_lines.json", 'w') as fp:
            json.dump(numbers, fp)


def compute_checked_coverable_lines(readable_file_path, lines, ignorable_strings):
    global file_path
    ignorable_strings = ignorable_strings.split(",")

    file_path = readable_file_path
    read_file()
    coverable_lines = []
    for idx, file_line in enumerate(file_contents):
        if int(idx + 1) in lines:
            cleaned_line = re.sub(r'\W+', '', file_line)
            if cleaned_line not in ignorable_strings:
                coverable_lines.append(idx + 1)

    return coverable_lines


def read_file():
    global file_contents
    if not path.exists(file_path):
        print("File not exist!" + file_path)
        file_contents = []
    else:
        f = open(file_path, encoding="ISO-8859-1")
        file_contents = f.read().splitlines()
        f.close()