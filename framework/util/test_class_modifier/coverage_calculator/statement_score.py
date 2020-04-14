from xml.dom import minidom
import json


def compute(xml_file_path, json_store_path):
    xml_doc = minidom.parse(xml_file_path)
    classes = xml_doc.getElementsByTagName('class')
    numbers = {}
    for current_class in classes:
        lines = current_class.getElementsByTagName('line')
        line_nr = []
        for line in lines:
            line_nr.append(int(line.attributes['number'].value))
        numbers[current_class.attributes['name'].value] = sorted(list(set(line_nr)))

    with open(json_store_path+"/line_coverage.json", 'w') as fp:
        json.dump(numbers, fp)
