import os
import json
from pick import pick
from simple_file import output_file, delete_file

filename = "tmp.json"


class Person:
    def __init__(self, d):
        self.__dict__ = d
    # def encoder(self):
    #     return {self.__class__.__name__: self.__dict__}


def add_data_to_json(data={}):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def merge(obj):
    try:
        with open(filename, "r") as file:
            data = json.load(file) | obj.__dict__
            return data
    except Exception as ex:
        print(ex)
        input("\n\nPress Enter to continue...")


def create_file():
    title = '[Add sample data to a file?]'
    options = ['Yes', 'No']
    option, index = pick(options, title, indicator='=>', default_index=0)
    match index:
        case 0:
            sample_data = {"Object": {"attr": "value", "attr2": {"1st": "1st value", "2nd": "2nd value"}, "attr3": [1, 2, 3]}}
            add_data_to_json(sample_data)
        case 1:
            add_data_to_json()


def create_new_object():
    os.system("cls")
    new_data = {}
    print("\nEnter an empty attribute name to stop\n")
    while True:
        key = input("Enter the name of attr: ")
        if key == "":
            break
        value = input("Enter value: ")
        new_data[key] = value
    new_obj = Person(new_data)

    title = '[Serialize to JSON and add an object to file?]'
    options = ['Yes', 'No']
    option, index = pick(options, title, indicator='=>', default_index=0)
    match index:
        case 0:
            try:
                data = merge(new_obj)
                print("\n\nData was merged.")
                add_data_to_json(data)
            except Exception as ex:
                os.system("cls")
                print(ex)
                input("\n\nPress Enter to continue...")
        case 1:
            pass


def submenu():
    title = '[Work with JSON file]'
    options = ['Create JSON file', 'Add new JSON lines', 'Output file', 'Delete file', 'Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def work_with_json():
    while True:
        match submenu():
            case 0:
                create_file()
                continue
            case 1:
                create_new_object()
                continue
            case 2:
                output_file(filename)
                continue
            case 3:
                delete_file(filename)
                continue
            case 4:
                break
