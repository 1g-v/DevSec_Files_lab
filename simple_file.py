import os
from pick import pick

filename = "tmp.txt"


def submenu():
    title = '[Work with ]'
    options = ['Create/clear file', 'Add line to file', 'Read file', 'Delete file', 'Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def create_new_file():
    os.system("cls")
    with open(filename, "w"):
        print("\nNew  created!")
    input("\n\nPress Enter to continue...")


def add_to_file():
    os.system("cls")
    print("Enter a lines to write (Ctrl+C to stop)")
    with open(filename, "a") as tmp:
        while True:
            try:
                tmp.write(str(input(">>> ")) + "\n")
            except KeyboardInterrupt:
                break
    input("\n\nPress Enter to continue...")


def output_file(filename):
    os.system("cls")
    try:
        with open(filename, "r") as tmp:
            for line in tmp.read().splitlines():
                print(line)
        input("\n\nPress Enter to continue...")
    except Exception as ex:
        print(ex)
        input("\n\nPress Enter to continue...")


def delete_file(filename):
    os.system("cls")
    try:
        path = os.path.abspath(filename)
        os.remove(path)
    except Exception as ex:
        print(ex)
        input("\n\nPress Enter to continue...")


def work_with_file():
    while True:
        match submenu():
            case 0:
                create_new_file()
                continue
            case 1:
                add_to_file()
                continue
            case 2:
                output_file(filename)
                continue
            case 3:
                delete_file(filename)
                continue
            case 4:
                break
