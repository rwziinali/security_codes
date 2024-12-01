def _pad_key(plaintext, key):
    # Function to pad the key to match the length of the plaintext
    padded_key = ''  # Initialize an empty string for the padded key
    i = 0  # Initialize an index for the key

    for char in plaintext:  # Loop through each character in the plaintext
        if char.isalpha():  # Check if the character is a letter
            padded_key += key[i % len(key)]  # Add the corresponding key character
            i += 1  # Increment the index for the key
        else:
            padded_key += ' '  # Add a space for non-letter characters

    return padded_key  # Return the padded key


def _encrypt_decrypt_char(plaintext_char, key_char, mode='encrypt'):
    # Function to encrypt or decrypt a single character based on the mode
    if plaintext_char.isalpha():  # Check if the character is a letter
        first_alphabet_letter = 'a'  # Default to lowercase
        if plaintext_char.isupper():  # Check if the character is uppercase
            first_alphabet_letter = 'A'  # Set to uppercase if needed

        old_char_position = ord(plaintext_char) - ord(
            first_alphabet_letter)  # Get the position of the plaintext character
        key_char_position = ord(key_char.lower()) - ord('a')  # Get the position of the key character

        if mode == 'encrypt':  # Check if the mode is encryption
            new_char_position = (
                                            old_char_position + key_char_position) % 26  # Calculate the new position for encryption
        else:  # Otherwise, it's decryption
            new_char_position = (
                                            old_char_position - key_char_position + 26) % 26  # Calculate the new position for decryption

        return chr(new_char_position + ord(first_alphabet_letter))  # Convert back to character and return it

    return plaintext_char  # Return the character unchanged if it's not a letter


def encrypt(plaintext, key):
    # Function to encrypt the entire plaintext using the key
    ciphertext = ''  # Initialize an empty string for the ciphertext
    padded_key = _pad_key(plaintext, key)  # Pad the key to the length of the plaintext

    for plaintext_char, key_char in zip(plaintext, padded_key):  # Loop through plaintext and padded key simultaneously
        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)  # Encrypt each character and add to ciphertext

    return ciphertext  # Return the final ciphertext


def decrypt(ciphertext, key):
    # Function to decrypt the ciphertext back to plaintext using the key
    plaintext = ''  # Initialize an empty string for the plaintext
    padded_key = _pad_key(ciphertext, key)  # Pad the key to the length of the ciphertext

    for ciphertext_char, key_char in zip(ciphertext,
                                         padded_key):  # Loop through ciphertext and padded key simultaneously
        plaintext += _encrypt_decrypt_char(ciphertext_char, key_char,
                                           mode='decrypt')  # Decrypt each character and add to plaintext

    return plaintext  # Return the final plaintext


# Main loop for the Vigenère cipher program
while True:
    print("\nVigenère Cipher")  # Print the title of the program
    print("1. Encrypt a message to Vigenère ")  # Option to encrypt a message
    print("2. Decrypt a message to plaintext")  # Option to decrypt a message
    print("3. Exit")  # Option to exit the program

    choice = input("Choose an option (1/2/3): ")  # Prompt user for their choice

    if choice == '1':  # If the user chooses to encrypt
        message = input('Enter a message to encrypt: ')  # Prompt for the message to encrypt
        key = input('Enter a key: ')  # Prompt for the encryption key
        result = encrypt(message, key)  # Call the encrypt function
        print(f'Ciphertext: {result}')  # Print the resulting ciphertext

    elif choice == '2':  # If the user chooses to decrypt
        message = input('Enter a message to decrypt: ')  # Prompt for the message to decrypt
        key = input('Enter a key: ')  # Prompt for the decryption key
        result = decrypt(message, key)  # Call the decrypt function
        print(f'Decrypted Plaintext: {result}')  # Print the resulting plaintext

    elif choice == '3':  # If the user chooses to exit
        print("Exiting the program.")  # Print exit message
        break  # Exit the loop and terminate the program

    else:  # If the input is invalid
        print("Please choose again.")  # Print message prompting the user to choose again
