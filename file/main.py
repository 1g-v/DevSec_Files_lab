from pick import pick
import os
from disk_info import disk_info
from simple_file import work_with_file


def main_menu():
    title = '1st lab | author: Igumenshchev Vasily | github: 1g-v'
    options = ['View disk info', 'Work with a text file']
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def main():
    while True:
        # index = main_menu()
        match main_menu():
            case 0:
                disk_info()
            case 1:
                work_with_file()
            case _:
                print("err")


if __name__ == '__main__':
    main()