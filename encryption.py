import base64
from datetime import datetime
from cryptography.fernet import Fernet
import file_operations

def encrypt(text, key):
    key=pad_string_to_32_bytes(key)
    key = base64.urlsafe_b64encode(key.encode("utf-8"))
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    #save_note function works with ascii, so we need to get rid of the binary version
    return encrypted_text.decode("ascii")

def decrypt(title,text, key):
    try:
        key=pad_string_to_32_bytes(key)
        key = base64.urlsafe_b64encode(key.encode("utf-8"))
        fernet = Fernet(key)
        decrypted_text = fernet.decrypt(text).decode()
        return decrypted_text
    except:
        # create a log text. including the date and time. and the title of the note
        log= f"Attemp to access {title} with wrong key at {datetime.now()}."
        file_operations.save_wrong_key_log(log)
        return ""

def pad_string_to_32_bytes(input_string):
    missing_bytes = 32 - len(input_string)
    if missing_bytes > 0:
        padded_string = input_string + "\0" * missing_bytes
        return padded_string
    elif len(input_string) == 32:
        return input_string
    else:
        return input_string[:32]