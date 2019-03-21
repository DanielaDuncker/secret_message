import os


def rename_files():
    path = r"/Users/Daniela/Downloads/prank 2"
    file_list = os.listdir(path)
    print(file_list)
    saved_path = os.getcwd()
    print("Current Wrorking Directory is " + saved_path)
    os.chdir(r"/Users/Daniela/Downloads/prank 2")

    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(str.maketrans("", "", "0123456789")))
        os.renames(file_name, file_name.translate(str.maketrans("", "", "0123456789")))
    os.chdir(saved_path)

rename_files()