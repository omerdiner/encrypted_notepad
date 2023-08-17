import os
import encryption

current_directory = os.getcwd()

def save_note_to_file(key_hint, note, title):
    #create a directory called notes if it doesn't exist
    if not os.path.exists(current_directory + "/notes"):
        os.mkdir(current_directory + "/notes")
    with open(current_directory + "/notes/" + title + ".txt", "w") as file:
        file.write(key_hint + "\n")
        file.write(note)

def get_note_from_file(title):
    with open(current_directory + "/notes/" + title + ".txt", "r") as file:
        key_hint = file.readline()
        #remove the \n from the end of the key hint
        key_hint = key_hint[:-1]
        note = file.read()
    return key_hint, note

def get_titles():
    if not os.path.exists(current_directory + "/notes"):
        return []
    #get all the files in the notes directory
    files = os.listdir(current_directory + "/notes")
    #remove the .txt from the end of each file
    files = [file[:-4] for file in files]
    return files

def delete_file(title):
    os.remove(current_directory + "/notes/" + title + ".txt")


def backup_notes():
    #create a directory called backup if it doesn't exist
    if not os.path.exists(current_directory + "/secret_backup"):
        os.mkdir(current_directory + "/secret_backup")

    files = os.listdir(current_directory + "/notes")
    for file in files:
        with open(current_directory + "/notes/" + file, "r") as original_file:
            with open(current_directory + "/secret_backup/" + file, "w") as backup_file:
                backup_file.write(original_file.read())






