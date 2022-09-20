import json


class Person:
    def __init__(self, d):
        self.__dict__ = d

    # def encoder(self):
    #     return {self.__class__.__name__: self.__dict__}


# data = {"Object": {"attr": "value", "attr2": {"1st": "1st value", "2nd": "2nd value"}, "attr3": [1, 2, 3]}}

new_data = {}
while True:
    key = input("Enter the name of attr: ")
    if key == "":
        break
    value = input("Enter value: ")
    new_data[key] = value


user = Person(new_data)


with open("tmp.json", "r") as file:
    data = json.load(file) | user.__dict__

with open("tmp.json", "w") as file:
    json.dump(data, file, indent=4)