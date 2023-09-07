import os
current_directory="C:/Users/OMER/PycharmProjects/encrypted_notepad"
#current_directory = os.getcwd()
wrong_key_log_file = "wrong_key_log.txt"


def save_note_to_file(key_hint, note, title):
    check_notes_dir()
    with open(current_directory + "/notes/" + title + ".txt", "w") as file:
        file.write(key_hint + "\n")
        file.write(note)


def get_note_from_file(title):
    with open(current_directory + "/notes/" + title + ".txt", "r") as file:
        key_hint = file.readline()
        # remove the \n from the end of the key hint
        key_hint = key_hint[:-1]
        note = file.read()
    return key_hint, note


def get_titles():
    if not os.path.exists(current_directory + "/notes"):
        return []
    # get all the files in the notes directory
    files = os.listdir(current_directory + "/notes")
    # remove the .txt from the end of each file
    files = [file[:-4] for file in files]
    return files


def delete_file(title):
    os.remove(current_directory + "/notes/" + title + ".txt")


def backup_notes():
    check_notes_dir()
    files = os.listdir(current_directory + "/notes")
    if len(files) == 0:
        return False
    check_backup_dir()

    for file in files:
        with open(current_directory + "/notes/" + file, "r") as original_file:
            with open(current_directory + "/secret_backup/" + file, "w") as backup_file:
                backup_file.write(original_file.read())

    return True


def save_wrong_key_log(log):
    check_log_dir()
    with open(current_directory + "/log/" + wrong_key_log_file, "a") as file:
        file.write(log + "\n")


def check_log_dir():
    if not os.path.exists(current_directory + "/log"):
        os.mkdir(current_directory + "/log")


def check_backup_dir():
    if not os.path.exists(current_directory + "/secret_backup"):
        os.mkdir(current_directory + "/secret_backup")


def check_notes_dir():
    if not os.path.exists(current_directory + "/notes"):
        os.mkdir(current_directory + "/notes")
