#! /usr/bin/env python3

"""just read the name this file just clear/delete all log files in current folder """
## import modules
from os import walk, getcwd
import os.path as path
from shutil import rmtree


#### USER INPUT
def get_user_input(prompt: str) -> str:
    """
    Get user input, returning it in lowercase with leading spaces removed.
    :param prompt: the text display
    :return: return the input of user(but lower case and removing the space at the begging)
    """
    return input(prompt).strip().lower()


#### REMOVE FOLDER
default_target: str = "__pycache__"


def remove_folder(folder_target: str = default_target) -> None:
    """ Remove specified folder [By default is`__pycache__`] in the current folder/directory and its subdirectories/subfolders.
    :param folder_target: The name of the folder to remove.
    """
    current_folder = getcwd()
    is_change_happen = False  # this check if there are change are apply or not (Remove Folder)

    for path_file, directory_name, _ in walk(current_folder):
        for d_name in directory_name:
            folder_cache_path = path.join(path_file, d_name)

            if d_name == folder_target:
                print(f"   | Removing :{folder_cache_path}")
                try:
                    ## Remove Folders (include all its contents)
                    rmtree(folder_cache_path)
                except (OSError, PermissionError) as error:
                    print(f"!!! Failed to Remove `{folder_cache_path}`: {error}")
                else:
                    is_change_happen = True

    if not is_change_happen:
        print(f">> There are no Folder that been Removed. check current folder/directory : {current_folder}")
    else:
        print(f">> Removed Folder have Completed")

    print(f">>> THE OPERATION HAVE COMPLETED")  # after Done all of this


#### MAIN FUNCTION
def main() -> None:
    """Main function to Execute"""
    yes: list[str] = ["y", "yes"]
    no: list[str] = ["n", "no"]
    default: list[str] = [""]
    chooses: list[str] = [*yes, *no, *default]
    user_input = get_user_input(
        f"--- Do you want to Remove(y)[Default] or Quit(n): "
    )

    while user_input not in chooses:  # Invalid input .Repeat
        print("Invalid input")
        user_input = get_user_input(
            f"--- Do you want to Remove(y)[Default] or Quit(n): "
        )

    if user_input in no:  # Quit
        print('OKAY Goodbye :]')
    else:
        folder_name: str = get_user_input(
            f"--- ENTER the NAME Folder [by default it's `{default_target}`]\n"
            f"   | Be Careful this will Remove also all Folder's contents: "
        )
        if not folder_name: folder_name = default_target  # Check if it's Empty (default)

        user_confirm = get_user_input(
            f"--- ARE YOU SURE you want to Remove any Folder's name `{folder_name}` \n"
            f"(yes|no): "
        )

        while (user_confirm not in chooses) or (not user_confirm):  # Invalid OR Empty input for Confirm .Repeat
            print("Invalid input")
            user_confirm = get_user_input(
                f"--- ARE YOU SURE you want to Remove any Folder's name `{folder_name}` \n"
                f"(yes|no): "
            )

        if user_confirm in yes:
            remove_folder(folder_name)  # Remove Folders
        else:  # if you change your mind :]
            print(f"So it seems I'll go to sleep. Okay :D")


#### Run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n!!! The task have been Terminated.\n")
