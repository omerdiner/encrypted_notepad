def encrypt(text,key):
    encrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text

def decrypt(text,key):
    decrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text