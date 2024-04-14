def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts text using Caesar Cipher.

  Args:
      text: The text to encrypt or decrypt.
      shift: The number of positions to shift letters.
      mode: 'encrypt' or 'decrypt'

  Returns:
      The encrypted or decrypted text.
  """
  result = ""
  for char in text:
    if char.isalpha():
      # Convert char to uppercase for easier handling
      char = char.upper()
      new_position = ord(char) + shift

      # Handle wrapping around the alphabet
      if mode == 'encrypt':
        new_position = new_position % 26 + 65
      else:
        new_position = new_position - 26 % 26 + 65
      result += chr(new_position)
    else:
      result += char
  return result

def main():
  """Prompts user for input and performs encryption/decryption."""
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      text = input("Enter the message to encrypt: ")
      shift = int(input("Enter the shift value (1-25): "))
      encrypted_text = caesar_cipher(text, shift, 'encrypt')
      print("Encrypted text:", encrypted_text)
    elif choice == '2':
      text = input("Enter the message to decrypt: ")
      shift = int(input("Enter the shift value (1-25): "))
      decrypted_text = caesar_cipher(text, shift, 'decrypt')
      print("Decrypted text:", decrypted_text)
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
