from xml.dom import minidom
import json


def compute(xml_file_path, json_store_path):
    xml_doc = minidom.parse(xml_file_path)
    classes = xml_doc.getElementsByTagName('class')

    output = {}
    for current_class in classes:
        class_name = current_class.attributes['name'].value
        methods = current_class.getElementsByTagName('method')
        numbers = {}
        for current_method in methods:
            method_name = current_method.attributes['name'].value
            lines = current_method.getElementsByTagName('line')
            line_nr = []
            for line in lines:
                if int(line.attributes['hits'].value) > 0:
                    line_nr.append(int(line.attributes['number'].value))
            numbers[method_name] = sorted(list(set(line_nr)))
        output[class_name] = numbers
            # numbers[class_name].append(numbers[method_name])

    with open(json_store_path+"/line_coverage.json", 'w') as fp:
        json.dump(output, fp)
