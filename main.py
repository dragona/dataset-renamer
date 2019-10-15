"""
My Dataset renamer
Used for renaming the folders and the files within them

How to use:
- place the dataset (folders) inside the "data" folder
- run the script

Input:


├── flag\ Afghanistan
│   ├── \ Afghanistan\ 1.shutterstock-194980604.jpg
│   ├── \ Afghanistan\ 10.765464_1.jpg
│   ├── \ Afghanistan\ 11.afghanistan-flag-heart-shaped-ribbon-vector-18538836.jpg
├── flag\ Albania
│   ├── \ Albania\ 1.flag-albania-260nw-470753921.jpg
│   ├── \ Albania\ 10.414r2HkVz%2BL._SR600%2C315_PIWhiteStrip%2CBottomLeft%2C0%2C35_SCLZZZZZZZ_.jpg
│   ├── \ Albania\ 11.1.jpg


Outcome:

├── afghanistan
│   ├── afghanistan_1.jpg
│   ├── afghanistan_10.jpg
│   ├── afghanistan_11.jpg
├── albania
│   ├── albania_1.jpg
│   ├── albania_10.jpg
│   ├── albania_11.jpg
"""

import os
import glob


def rename_data_folders():
    """
    set folder names to lower and replace space to _
    """
    list_ = os.listdir('data')  # get all the folder names
    for f_name in list_:
        if f_name.startswith("."): continue  # skip hidden files
        new_name = ("_".join(f_name.split()[1:])).lower()  # skip the word "flag "
        if len(new_name) == 0: continue
        os.rename('./data/' + f_name, './data/' + new_name)
        print(f_name, "===>", new_name)


def rename_image():
    """
    Rename the image using the folder name and a number
    :return:
    """
    list_ = os.listdir('data')  # get all the folder names
    for folder_name in list_:
        if folder_name.startswith("."): continue  # skip hidden files
        # get the list of file inside the folder
        path = os.getcwd() + "/data/" + folder_name
        list_files = glob.glob(path + "/*")
        print(list_files)
        counter = 1
        for file_name in list_files:
            extension = file_name.split(".")[-1]
            new_name = f'{folder_name}_{counter}.{extension}'
            # file_name = file_name.strip()
            os.rename(file_name, path + "/" + new_name)
            print(file_name, "===>", new_name)
            counter += 1


if __name__ == '__main__':
    rename_data_folders()
    rename_image()
