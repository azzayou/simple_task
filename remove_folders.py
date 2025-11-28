"""just read the name this file just clear/delete all log files in current folder """
## import modules
import os
import os.path as path
from shutil import rmtree

#### INPUT USER
def Get_user_input(prompt: str) -> str:
    """
    :param prompt: the text display
    :return: return the input of user(but lower case and removing the space at the begging)
    """
    return input(prompt).strip().lower()  # :| this is weird

#### REMOVE/CLEAR FOLDER
def remove_folder(folder_target: str = "__pycache__") -> None:
    """ Remove any folders like `__pycache__` only in current folder (sub folders are included)
    :param folder_target: by default it `__pycache__` folder
    """
    current_folder = os.getcwd() # get current folder/directory
    is_change_happen = False # this check if there are change are apply (Remove Folder) 

    for path_file, directory_name, _ in os.walk(current_folder):
        for d_name in directory_name:
            folder_cache_path = path.join(path_file, d_name)

            if d_name == folder_target:
                print(f"   | Removing :{folder_cache_path}")
                try:
                    ## Remove Folders (include all its contents)
                    rmtree(folder_cache_path)
                
                except (OSError, PermissionError) as error:
                    print(f"!!! Failed to Remove `{folder_cache_path}`: {error}")

    if not is_change_happen:
        print(f">> There are no Folder that been Removed. check current folder/directory : {current_folder}")
    else:
        print(f">> Removed Folder have Completed")

    print(f">>> THE OPERATION HAVE COMPLETED") # after Done all of this

#### MAIN FUNCTION
def Main():
    """ that run to get input from user then Do dependent on his input"""
    chooses: list[str] = ["y", "", "n","q"]  # y = Yes [Default] , q/n = Quit
    user_input = Get_user_input(
        f"--- Do you want to Remove(y)[Default] or Quit(n/q) \n"
        f"   | Be Carefull this will Remove all Folder include all its contents :"
    )

    while user_input not in chooses:  # Invalid input .repeat
        print("Invalid input")
        user_input = Get_user_input(
            f"--- Do you want to Remove(y)[Default] or Quit(n/q): "
        )

    if user_input in ["n", "q"]:  # Quit
        print('SO Goodbye :]')
    else:  # REMOVE FOLDERS cache
        user_confirm = Get_user_input(
            f"--- ARE YOU SURE you want to Remove (yes|no): "
        )

        while user_input not in chooses:  # Invalid input to Confirm .repeat
            print("Invalid input")
            user_input = Get_user_input(
                f"--- ARE YOU SURE you want to Remove (yes|no): "
            )

        if user_confirm in ["y", "yes"]:
            remove_folder() # Remove Folders cache
        else:  # if you change your mind :]
            print(f"So it seems I'll go to sleep. Okay :D")

#### Run
if __name__ == "__main__":
    Main()
