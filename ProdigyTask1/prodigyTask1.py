def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Encrypt and Decrypt Text using the Caesar Cipher Algorithm")
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print(f"Encrypted text: {encrypted_text}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()