import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog

import encryption
import file_operations



def check_if_title_exists(title):
    titles = file_operations.get_titles()
    if title in titles:
        messagebox.showerror(title="Error", message="A note with this title already exists!")
        return True
    else:
        return False


def check_entries():
    if len(title_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Please enter a title for your note!")
        return False
    elif len(note_entry.get("1.0", tk.END)) == 1:
        messagebox.showerror(title="Error", message="Please enter a note!")
        return False
    else:
        return check_if_title_exists(title_entry.get()) == False


def check_key(key):
    if len(key) == 0:
        messagebox.showerror(title="Error", message="Please enter a key!")
        return False
    else:
        return True


def take_key():
    key = simpledialog.askstring(title="Key", prompt="What's your secret key?:", show='*', initialvalue="*********")
    return key


def take_key_hint():
    key_hint = simpledialog.askstring(title="Hint", prompt="Hint:", initialvalue="Be creative!")
    return key_hint

def if_note_exists():
    titles = file_operations.get_titles()
    return len(titles) > 0

def encrypt_note():
    if not check_entries():
        return
    key = take_key()
    if not check_key(key):
        return

    key_hint = take_key_hint()

    encrypted_note = encryption.encrypt(note_entry.get("1.0", tk.END), key)
    title = title_entry.get()
    file_operations.save_note_to_file(key_hint, encrypted_note, title)
    messagebox.showinfo(title="Note saved", message="Your note has been saved successfully!")
############################################################################

def open_decryption_window():

    if if_note_exists()==False:
       messagebox.showerror(title="Error", message="There are no notes to decrypt!")
       return


    decrypt_window = tk.Toplevel(main_window)
    decrypt_window.title("Decryption")
    decrypt_window.geometry("700x700")
    decrypt_window.config(padx=20, pady=20)

    info_label= tk.Label(decrypt_window,text="Choose the note you want to decrypt")
    info_label.config(font=("Arial", 24, "bold"))
    info_label.pack()

    titles = file_operations.get_titles()
    titles.sort()
    listbox = tk.Listbox(decrypt_window, selectmode=tk.SINGLE)
    listbox.config(font=("Arial", 24, "bold"))
    # change the color of the selected item
    listbox.config(selectbackground="red")
    listbox.pack(expand=True)

    for title in titles:
        listbox.insert(tk.END, title)

    hint_label = tk.Label(decrypt_window, text="Hint")
    hint_label.config(font=("Arial", 24, "bold"))
    hint_label.pack()

    key_label = tk.Label(decrypt_window, text="Key")
    key_label.config(font=("Arial", 24, "bold"))
    key_label.pack()

    key_entry = tk.Entry(decrypt_window)
    key_entry.config(font=("Arial", 24, "bold"))
    key_entry.pack()

    decrypt_button = tk.Button(decrypt_window, text="Decrypt")
    decrypt_button.config(font=("Arial", 24, "bold"))
    decrypt_button.pack()

    ##TO-DO
    # CLICKING ON THE TITLE FROM THE LIST WILL CHANGE THE HINT LABEL
    # PRESSING DECRYPT WILL OPEN A NEW PAGE AND SHOW THE NOTE IN WHITE TEXT ON A DARK BACKGROUND


#########################################################################

main_window = tk.Tk()
main_window.title("Top Secret")
main_window.geometry("700x700")
main_window.config(padx=20, pady=20)

# adding an image
image_path = "secret.png"
img = tk.PhotoImage(file=image_path)
app_photo = tk.Label(main_window, image=img)
app_photo.pack()

# label for the title
title_label = tk.Label(text="Title of the note")
title_label.config(font=("Arial", 24, "bold"))
title_label.pack()

# entry for title
title_entry = tk.Entry()
title_entry.config(font=("Arial", 24, "bold"))
title_entry.pack()

# label for the note
note_label = tk.Label(text="Note")
note_label.config(font=("Arial", 24, "bold"))
note_label.pack()

# text entry for the note
note_entry = tk.Text()
note_entry.config(font=("Arial", 24, "bold"))
note_entry.config(height=8, width=40)
note_entry.pack()
note_entry.focus()

# encryption
encrypt_button = tk.Button(text="Encrypt", command=encrypt_note)
encrypt_button.config(font=("Arial", 24, "bold"))
encrypt_button.pack()

# decryption
###TO-DO - add functionality to the button -> get the decryption page for the user to choose the note to decrypt #
decrypt_button = tk.Button(text="Decrypt", command=open_decryption_window)
decrypt_button.config(font=("Arial", 24, "bold"))
decrypt_button.pack()





main_window.mainloop()
