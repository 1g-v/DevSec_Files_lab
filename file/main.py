from pick import pick
import os
from disk_info import disk_info
from simple_file import work_with_file
from json_file import work_with_json


def main_menu():
    title = '1st lab | author: Igumenshchev Vasily | github: 1g-v'
    options = ['View disk info', 'Work with a text file', 'Work with a JSON file']
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def main():
    while True:
        match main_menu():
            case 0:
                disk_info()
            case 1:
                work_with_file()
            case 2:
                work_with_json()
            case _:
                print("err")


if __name__ == '__main__':
    main()
