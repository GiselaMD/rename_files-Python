import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\alphabet")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\alphabet")
    new_path = os.getcwd()
    print("Current Working Directory is "+new_path)
    
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    print("Current Working Directory is "+saved_path)
rename_files()
