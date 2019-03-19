import os


def rename_files():
    path = r"/Users/Daniela/Downloads/prank/"
    file_list = os.listdir(path)
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"/Users/Daniela/Downloads/prank/")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans("0123456789", ",,,,,,,,,,")))
    os.chdir(saved_path)


rename_files()
