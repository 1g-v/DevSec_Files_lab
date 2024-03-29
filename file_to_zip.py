import os
import zipfile
from pick import pick
from simple_file import delete_file

zip_name = "tmp_archive.zip"


def create_zip():
    os.system("cls")
    with open(zip_name, "w"):
        print("\nNew zip-archive was created!")
    input("\n\nPress Enter to continue...")


def write_to_zip(filename):
    with zipfile.ZipFile(zip_name, "a") as zip_f:
        zip_f.write(filename)


def extract_from_zip(filename):
    with zipfile.ZipFile(zip_name, "r") as zip_f:
        zip_f.extract(filename, path="../files/extracted_files")


def submenu():
    title = '[Work with zip-archive]'
    options = ['Create zip-archive', 'Add file to zip', 'Extract file from zip', 'Delete zip', 'Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def pick_file(file_list):
    title = '[Select a file]'
    option, index = pick(file_list, title, indicator='=>', default_index=0)
    return option


def work_with_zip():
    while True:
        match submenu():
            case 0:
                create_zip()
                continue
            case 1:
                write_to_zip(pick_file(os.listdir()))
            case 2:
                extract_from_zip(pick_file(zipfile.ZipFile(zip_name).namelist()))
                continue
            case 3:
                delete_file(zip_name)
                continue
            case 4:
                break
