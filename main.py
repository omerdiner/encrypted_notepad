import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog
import encryption
import file_operations

##TO-DO  MAKE ENCRIPTION TURKISH ALPHABET FRIENDLY

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
def open_decrypted_note(title,key):

    show_decrypted_note_window = tk.Toplevel(main_window)
    show_decrypted_note_window.title(title)
    show_decrypted_note_window.geometry("700x700")
    show_decrypted_note_window.config(padx=20, pady=20)
    show_decrypted_note_window.config(bg="dark blue")

    note=file_operations.get_note_from_file(title)[1]
    decrypted_note=encryption.decrypt(note,key)

    decrypted_note_text = tk.Text(show_decrypted_note_window, height=20, width=50)
    decrypted_note_text.config(font=("Arial", 24, "bold"))
    decrypted_note_text.insert(tk.END, decrypted_note)
    decrypted_note_text.pack()


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
    listbox.config(fg="dark gray")
    # change the color of the selected item
    listbox.config(selectbackground="red")
    listbox.pack(expand=True)

    for title in titles:
        listbox.insert(tk.END, title)

    def callback(event):
        selection = event.widget.curselection()
        global clicked_title
        if selection:
            index = selection[0]
            clicked_title = event.widget.get(index)

        selected_hint=file_operations.get_note_from_file(clicked_title)[0]
        hint_text="Hint : "+'"'+selected_hint+'"'
        hint_label.config(text=hint_text)

    listbox.bind("<<ListboxSelect>>", callback)

    hint_label = tk.Label(decrypt_window, text="Hint")
    hint_label.config(font=("Arial", 20, "bold"))
    hint_label.config(padx=20, pady=20)
    hint_label.pack()

    key_label = tk.Label(decrypt_window, text="Key")
    key_label.config(font=("Arial", 18, "bold"))
    key_label.pack(side="left")
    key_label.config(padx=20)

    key_entry = tk.Entry(decrypt_window)
    key_entry.config(font=("Arial", 24, "bold"))
    key_entry.pack(side="left")
    key_entry.focus()

    decrypt_button = tk.Button(decrypt_window, text="Decrypt",command=lambda : open_decrypted_note(clicked_title,key_entry.get()))
    decrypt_button.config(font=("Arial", 24, "bold"))
    decrypt_button.pack()

    def delete_note(title):
        answer = messagebox.askyesno(title="Delete",
                                     message="Are you sure you want to delete the {}.txt ?".format(title))
        if answer == False:
            return
        else:
            file_operations.delete_file(title)
            messagebox.showinfo(title="Note deleted", message="Your note has been deleted successfully!")
            decrypt_window.destroy()

    delete_button = tk.Button(decrypt_window, text="Delete",command=lambda : delete_note(clicked_title))
    delete_button.config(font=("Arial", 24, "bold"))
    delete_button.pack()



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
