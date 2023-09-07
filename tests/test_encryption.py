from encryption import encrypt, decrypt, pad_string_to_32_bytes

def test_encrypt_decrypt():
    key = "my_secret_key"
    original_text = "Hello, World!"
    key2= "43_230??34SDMlld"
    original_text2 = "This is a LONGER and more COMPLICATED text. It should be encrypted and decrypted correctly. -123"

    encrypted_text = encrypt(original_text, key)
    decrypted_text = decrypt("hint",encrypted_text, key)

    encrypted_text2 = encrypt(original_text2, key2)
    decrypted_text2 = decrypt("hint",encrypted_text2, key2)

    assert decrypted_text == original_text
    assert decrypted_text2 == original_text2

def test_pad_string_to_32_bytes():
    input_string = "short_string"
    padded_string = pad_string_to_32_bytes(input_string)

    assert len(padded_string) == 32
    assert padded_string.startswith(input_string)

    long_input = "a_long_input_string_that_is_longer_than_32_characters"
    padded_long_string = pad_string_to_32_bytes(long_input)

    assert len(padded_long_string) == 32
    assert padded_long_string == long_input[:32]

if __name__ == "__main__":
    test_encrypt_decrypt()
    test_pad_string_to_32_bytes()
