import tkinter as tk

create_window = tk.Tk()
create_window.title("Secret Notes")
create_window.geometry("700x700")
create_window.config(padx=20, pady=20)

#adding an image
image_path = "secret.png"
img = tk.PhotoImage(file=image_path)
app_photo = tk.Label(create_window, image=img)
app_photo.pack()

#add a label for the title
title_label = tk.Label(text="Title of the note")
title_label.config(font=("Arial", 24, "bold"))
title_label.pack()

#entry for title
title_entry = tk.Entry()
title_entry.config(font=("Arial", 24, "bold"))
title_entry.pack()

#add a label for the note
note_label = tk.Label(text="Note")
note_label.config(font=("Arial", 24, "bold"))
note_label.pack()

#text entry for the note
note_entry = tk.Text()
note_entry.config(font=("Arial", 24, "bold"))
note_entry.config(height=8, width=40)
note_entry.pack()

#add a button to encrypt the note
###TO-DO - add functionality to the button -> call the encrypt function from encryption.py and save the encrypted note to a file#
encrypt_button = tk.Button(text="Encrypt")
encrypt_button.config(font=("Arial", 24, "bold"))
encrypt_button.pack()

#add a button to decrypt the note
###TO-DO - add functionality to the button -> get the decryption page for the user to choose the note to decrypt #
decrypt_button = tk.Button(text="Decrypt")
decrypt_button.config(font=("Arial", 24, "bold"))
decrypt_button.pack()


create_window.mainloop()

