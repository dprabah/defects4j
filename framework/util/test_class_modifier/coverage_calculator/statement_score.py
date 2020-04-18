from xml.dom import minidom
import json
import os.path


def compute(xml_file_path, json_store_path, executed_method):
    # executed_method = executed_method.split("::")[1]
    xml_doc = minidom.parse(xml_file_path)
    classes = xml_doc.getElementsByTagName('class')
    file_path = json_store_path+"/line_coverage.json"
    output = {}
    if os.path.exists(file_path):
        with open(file_path) as fp:
            output = json.load(fp)

    for current_class in classes:
        class_name = current_class.attributes['name'].value
        methods = current_class.getElementsByTagName('method')
        numbers = {}
        for current_method in methods:
            # method_name = current_method.attributes['name'].value
            method_name = str(executed_method)
            lines = current_method.getElementsByTagName('line')
            line_nr = []
            for line in lines:
                if int(line.attributes['hits'].value) > 0:
                    line_nr.append(int(line.attributes['number'].value))
            if line_nr.__len__() > 0:
                numbers[method_name] = sorted(list(set(line_nr)))
        if numbers.__len__() > 0:
            try:
                output[class_name].update(numbers)
            except KeyError:
                output[class_name] = numbers
            # numbers[class_name].append(numbers[method_name])

    with open(file_path, 'w') as fp:
        json.dump(output, fp)
