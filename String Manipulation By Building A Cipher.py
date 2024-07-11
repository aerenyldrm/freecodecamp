text = "Greetings Nihan"
optional_key = "beautiful"
def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    key_index = 0
    for character in message.lower():
        # append any non-letter character to the message
        if not character.isalpha():
            final_message += character
        else:
            # find the correct key character to encode/decode
            key_character = key[key_index % len(key)]
            key_index += 1
            # define the offset and the encrypted/decrypted letter
            current_index = alphabet.find(character)
            offset = alphabet.index(key_character)
            final_message += alphabet[(current_index + offset * direction) % len(alphabet)]
    return final_message
def encrypt(message, key):
    return vigenere(message, key)
def decrypt(message, key):
    return vigenere(message, key, -1)
encryption = encrypt(text, optional_key)
print(f"encrypted text is '{encryption}'.")
decryption = decrypt(encryption, optional_key)
print(f"decrypted message is '{decryption}'.")