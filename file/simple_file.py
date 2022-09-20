from pick import pick
import os


def submenu():
    title = '[Work with file]'
    options = ['Create/clear temp file', 'Add line to file', 'Output file', 'Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def create_new_file():
    os.system("cls")
    with open("tmp.txt", "w"):
        print("\nNew file created!")
    input("\n\n => Back")


def add_to_file():
    os.system("cls")
    print("Enter a lines to write (Ctrl+C to stop)")
    with open("tmp.txt", "a") as tmp:
        while True:
            try:
                tmp.write(str(input(">>> ")) + "\n")
            except KeyboardInterrupt:
                break
    input("\n\n => Back")


def output_file():
    os.system("cls")
    with open("tmp.txt", "r") as tmp:
        for line in tmp.read().splitlines():
            print(line)
    input("\n\n => Back")


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
                output_file()
                continue
            case 3:
                break
