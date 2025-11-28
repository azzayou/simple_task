"""just read the name this file just clear/delete all log files in current folder """
## import modules
import os
import os.path as path

#### INPUT USER
def Get_user_input(prompt: str) -> str:
    """
    :param prompt: the text display
    :return: return the input of user(but lower case and removing the space at the begging)
    """
    return input(prompt).strip().lower()  # :| this is weird

#### REMOVE/CLEAR LOG FILES
def Clear_Log_Files(remove: bool = False, file_format: str = "log") -> None:
    """ Remove any log files only in current folder (sub folders are included)
    :param remove: option to remove or clear (True to remove False to Clear)
    :param file_format: by default it `log` file
    """
    current_folder = os.getcwd() # get current folder/directory
    is_change_happen = False # this check if change apply (Remove or Clear log files)

    for path_file, _, files_name in os.walk(current_folder):
        for f_name in files_name:
            log_file_path = path.join(path_file, f_name)

            if f_name.endswith(f".{file_format}"):
                print(f"   | {'Removing' if remove else 'Clearing'} :{log_file_path}")
                try:
                    if remove: # Remove log Files
                        os.remove(log_file_path)
                        is_change_happen = True

                    else:  # Clear log Files
                        with open(log_file_path, "w") : pass
                        is_change_happen = True

                except (OSError, PermissionError) as error:
                    print(f"!!! Failed to {'Remove' if remove else 'Clear'} `{log_file_path}`: {error}")

    if not is_change_happen:
        print(f">> There are no log file that {'been Removed' if remove else 'were Cleared'}. check folder: {current_folder}")
    else:
        print(f">> {'Removed' if remove else 'Cleared'} log Files have Completed")

    print(f">>> THE OPERATION HAVE COMPLETED") # after Done all of this

#### MAIN FUNCTION
def Main():
    """ that run to get input from user then Do dependent on his input"""
    chooses: list[str] = ["y", "n", "", "q"]  # y = Yes(Remove), n = No(just Clear)(and Default), q = Quit
    user_input = Get_user_input(
        f"--- Do you want to Remove(y), Clear(n)[Default] or Quit(q): "
    )

    while user_input not in chooses:  # Invalid input .repeat
        print("Invalid input")
        user_input = Get_user_input(
            f"--- Do you want to Remove(y), Clear(n)[Default] or Quit(q): "
        )

    if user_input == "q":  # Quit
        print('SO Goodbye :]')
    else:  # Clear or Remove log Files
        want_remove = (user_input == "y")
        user_confirm = Get_user_input(
            f"--- ARE YOU SURE you want to {'Remove' if want_remove else 'Clear'} (yes|no):"
        )

        while user_input not in chooses:  # Invalid input .repeat
            print("Invalid input")
            user_input = Get_user_input(
                f"--- Do you want to Remove(y), Clear(n)[Default] or Quit(q): "
            )

        if user_confirm in ["y", "yes"]:
            if want_remove:  # Remove
                Clear_Log_Files(remove=True)
            else:  # Clear
                Clear_Log_Files()
        else:  # if you change your mind :]
            print(f"So it seems I'll go to sleep. Okay :D")

#### Run
if __name__ == "__main__":
    Main()
