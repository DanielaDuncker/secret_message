import os

def rename_files():
    file_list = os.listdir(r"/Users/Daniela/Downloads/prank/")
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"/Users/Daniela/Downloads/prank/")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "123456789"))
    os.chdir(saved_path)

rename_files()

