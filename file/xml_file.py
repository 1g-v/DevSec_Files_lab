import xml.etree.ElementTree as ET
from pick import pick
import os


def create_xml():
    title = '[Add sample data to a file?]'
    options = ['Yes', 'No']
    option, index = pick(options, title, indicator='=>', default_index=0)
    match index:
        case 0:
            sample_data = ET.fromstring('<catalog>'
                                        '<object eatable="yes">banana</object>'
                                        '<object eatable="no">car</object>'
                                        '<element><subelement1>text1</subelement1>'
                                        '<subelement2><description exist="False" /></subelement2>'
                                        '</element></catalog>')
            add_to_xml(sample_data)
        case 1:
            sample_data = ET.fromstring('<root></root>')
            add_to_xml(sample_data)


def create_subelement():
    root = ET.parse('tmp.xml').getroot()
    parent = root
    while True:
        element_name = input(f"Enter the name of <{parent.tag}> subelement : ")
        if element_name == "":
            break
        attrs = {}
        while True:
            key = input(f"Enter the name of attribute of <{element_name}> : ")
            if key == "":
                break
            value = input(f'Enter the "{key}" value: ')
            attrs[key] = value
        text = input(f"Enter text for <{element_name}>: ")
        new_element = ET.SubElement(parent, element_name, attrs)
        new_element.text = text
        parent = new_element
    add_to_xml(root)


def add_to_xml(root):
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write("tmp.xml", xml_declaration=True, encoding='utf-8')


def submenu():
    title = '[Work with XML file]'
    options = ['Create simple XML file', 'Add new element to XML', 'Output file', 'Delete file', 'Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def output_file():
    os.system("cls")
    try:
        with open("tmp.xml", "r") as tmp:
            for line in tmp.read().splitlines():
                print(line)
        input("\n\n => Back")
    except Exception as ex:
        print(ex)
        input("\n\nPress Enter to continue...")


def delete_file():
    os.system("cls")
    try:
        path = os.path.abspath('tmp.xml')
        os.remove(path)
    except Exception as ex:
        print(ex)
        input("\n\nPress Enter to continue...")


def work_with_xml():
    while True:
        match submenu():
            case 0:
                create_xml()
            case 1:
                create_subelement()
            case 2:
                output_file()
            case 3:
                delete_file()
            case 4:
                break
