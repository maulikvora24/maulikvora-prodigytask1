def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift)

def decrypt(text, shift):
    return caesar_cipher(text, -shift)

# Main program
def main():
    choice = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n").lower()
    text = input("Enter your message:\n")
    shift = int(input("Enter the shift number:\n"))
    
    if choice == 'encrypt':
        print("Encrypted text:", encrypt(text, shift))
    elif choice == 'decrypt':
        print("Decrypted text:", decrypt(text, shift))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
