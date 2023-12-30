"""
Batch Rename - Caleb hair & Daniel Mackle
"""
# imports
from tkinter import filedialog, messagebox
from tkinter.simpledialog import askstring
from os import listdir, rename
from os.path import splitext


def check_if_name_contains_angles(name: str) -> bool:
    if "<>" in name:
        return True
    return False


def take_folder() -> str:
    """
    Displays messagebox
    then opens file manager to input folder
    :return: str name - if invalid returns '/'
    """
    messagebox.showinfo("Batch Rename", "Hello!\nPlease choose a folder to rename all of your files "
                                        "in.")
    return filedialog.askdirectory() + "/"


def rename_file(folder__: str, name_: str, count_: int, filename_: str) -> None:
    filepath = folder__ + filename_  # append file root to file name to create full filepath
    extension = splitext(filepath)[-1]  # take extension from original filepath and isolate it - takes the '.'
    new_filepath = folder__ + name_.replace("<>", str(count_))  # replace instance of <> with count
    rename(filepath, new_filepath + extension)  # rename the file


def rename_all_files(folder_: str, name_: str) -> None:
    list_of_names = listdir(folder_)  # take all files from given folder
    for count, filename in enumerate(list_of_names):  # enumerate takes index and value of each file in the folder
        count += 1  # initialise to 1
        rename_file(folder_, name_, count, filename)


if __name__ == '__main__':
    try:
        folder = take_folder()  # '/' if null
        if folder == "/":  # if folder is invalid, exit
            exit()  # close program
        name = askstring("Batch Rename", "Thank you! Please enter a name for your renamed files.\n"
                                         "Within the name please contain <> to be replaced with the number beginning "
                                         "with 1.")
        if not check_if_name_contains_angles(name):
            messagebox.showerror("Batch Rename", "Sorry! You must include <> in your prompt.")
            exit();
        rename_all_files(folder, name)
    except FileExistsError:  # if contains invalid character - close
        messagebox.showerror("Batch Rename", "Sorry! The renaming has failed.\nPlease try again!")
