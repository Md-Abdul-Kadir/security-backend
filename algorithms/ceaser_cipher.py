def caesar_encryption(input_text,key):
    # key = int(input("Enter the key value (integer): "))
    # input_text = input_text_from_file("/content/in.txt")
    cipher_text = ""
    for char in input_text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            cipher_text += encrypted_char
        else:
            cipher_text += char
    # output_text_to_file("/content/out.txt", cipher_text)
    return cipher_text
    # print("Encrypted text written to out.txt")

def caesar_decryption(cipher_text,key):
    # key = int(input("Enter the key value (integer): "))
    # cipher_text = input_text_from_file("/content/in.txt")
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plain_text += decrypted_char
        else:
            plain_text += char
    # output_text_to_file("/content/out.txt", plain_text)
    return plain_text
    print("Decrypted text written to out.txt")