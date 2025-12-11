#! /usr/bin/env python3

"""just read the name this file just clear/delete all log files in current folder """
## import modules
from os import walk, getcwd, remove
import os.path as path


#### INPUT USER
def get_user_input(prompt: str) -> str:
    """Get user input, returning it in lowercase with leading spaces removed.
    :param prompt: the text display
    :return: return the input of user(but lower case and removing the space at the begging)
    """
    return input(prompt).strip().lower()  # :| this is weird


#### REMOVE/CLEAR FILES
default_file_format: str = "log"


def Clear_Log_Files(want_remove: bool = False, file_format: str = default_file_format) -> None:
    """ Remove any log files only in current folder (sub folders are included)
    :param want_remove: option to remove if it's True otherwise it's just clear
    :param file_format: by default it `log` file
    """
    current_folder = getcwd()  # get current folder/directory
    is_change_happen = False  # this check if change apply (Remove or Clear log files)

    for the_path, _, files_name in walk(current_folder):
        for f_name in files_name:
            log_file_path = path.join(the_path, f_name)

            if f_name.endswith(f".{file_format}"):
                print(f"   | {'Removing' if want_remove else 'Clearing'} :{log_file_path}")
                try:
                    if want_remove:  # Remove log Files
                        remove(log_file_path)

                    else:  # Clear log Files
                        with open(log_file_path, "w"):
                            pass

                except (OSError, PermissionError) as error:
                    print(f"!!! Failed to {'Remove' if want_remove else 'Clear'} `{log_file_path}`: {error}")
                else:
                    is_change_happen = True

    if not is_change_happen:
        print(
            f">> There are no file that {'been Removed' if want_remove else 'were Cleared'}. check folder: {current_folder}")
    else:
        print(f">> {'Removed' if want_remove else 'Cleared'} Files have Completed")

    print(f">>> THE OPERATION HAVE COMPLETED")  # after Done all of this


#### MAIN FUNCTION
def Main() -> None:
    """THE MAIN FUNCTION to Execute"""
    yes: list[str] = ["y", "yes"]
    no: list[str] = ["n", "no"]
    leave: list[str] = ["q", "quit"]
    default: list[str] = [""]
    chooses: list[str] = [*yes, *no, *leave, *default]  # y = Yes(Remove), n = No(just Clear)(and Default), q = Quit
    user_input = get_user_input(
        f"--- Do you want to Remove(y), Clear(n)[Default] or Quit(q): "
    )

    while user_input not in chooses:  # Invalid input .repeat
        print("Invalid input")
        user_input = get_user_input(
            f"--- Do you want to Remove(y), Clear(n)[Default] or Quit(q): "
        )

    if user_input == leave:  # Quit
        print('SO Goodbye :]')
    else:  # Clear or Remove log Files
        want_to_remove = (user_input in yes)
        the_file_format = get_user_input(
            f"--- ENTER the FILE FORMAT [by default it's `{default_file_format}`]\n"
            f"   | Be Careful this will Remove any File in current folder/directory: "
        )
        if not the_file_format: the_file_format = default_file_format  # Check if it's empty (default)

        user_confirm = get_user_input(
            f"--- ARE YOU SURE you want to {'Remove' if want_to_remove else 'Clear'} \n"
            f"All Files that end with `{the_file_format}` (yes|no):"
        )

        while (user_confirm not in chooses) or (not user_confirm):  # Invalid or Empty input to Confirm .repeat
            print("Invalid input")
            user_confirm = get_user_input(
                f"--- ARE YOU SURE you want to {'Remove' if want_to_remove else 'Clear'} \n"
                f"All Files that end with `{the_file_format}` (yes|no):"
            )

        if user_confirm in yes:
            Clear_Log_Files(file_format=the_file_format, want_remove=want_to_remove)
        else:  # if you change your mind :]
            print(f"So it seems I'll go to sleep. Okay :D")


#### Run
if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print("\n!!! THE TASK HAVE BEEN STOPPED\n")