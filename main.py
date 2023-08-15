import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import encryption
import file_operations


def check_entries():
    if len(title_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Please enter a title for your note!")
        return False
    elif len(note_entry.get("1.0", tk.END)) == 1:
        messagebox.showerror(title="Error", message="Please enter a note!")
        return False
    else:
        return True


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


create_window = tk.Tk()
create_window.title("Top Secret")
create_window.geometry("700x700")
create_window.config(padx=20, pady=20)

# adding an image
image_path = "secret.png"
img = tk.PhotoImage(file=image_path)
app_photo = tk.Label(create_window, image=img)
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
###TO-DO CHECK IF THE FILE WITH THE SAME NAME ALREADY EXISTS
encrypt_button = tk.Button(text="Encrypt", command=encrypt_note)
encrypt_button.config(font=("Arial", 24, "bold"))
encrypt_button.pack()

# decryption
###TO-DO - add functionality to the button -> get the decryption page for the user to choose the note to decrypt #
decrypt_button = tk.Button(text="Decrypt")
decrypt_button.config(font=("Arial", 24, "bold"))
decrypt_button.pack()

create_window.mainloop()
