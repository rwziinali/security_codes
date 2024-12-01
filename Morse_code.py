# Dictionary containing Morse code representations for each letter and number
MORSE_CODE_DICT1 = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', '/': ' '
}
# Dictionary containing letters corresponding to each Morse code
MORSE_CODE_DICT2 = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '-----': '0', ' ': '/'
}

# Infinite loop to allow user options
while True:
    print("\nMorse Code Converter")  # Print the program title
    print("1. Encrypt plaintext to Morse code")  # Option to encrypt text
    print("2. Decrypt Morse code to plaintext")  # Option to decrypt Morse code
    print("3. Exit")  # Option to exit the program

    choice = input("Choose an option (1/2/3): ")  # Prompt user for their choice

    if choice == '1':  # If the user chooses to encrypt text
        MORSE_CODE = ""  # Initialize variable to store the resulting Morse code
        text = input("Enter the plaintext message: ")  # Prompt user for plaintext input
        for transfer in text:  # Loop through each character in the text
            CODE = MORSE_CODE_DICT1.get(transfer.upper())  # Get Morse code for the character
            MORSE_CODE = MORSE_CODE + " " + CODE  # Add the code to the result with a space
        print("Encrypted Morse Code:", MORSE_CODE)  # Print the resulting Morse code

    elif choice == '2':  # If the user chooses to decrypt Morse code
        PLAINTEXT = ""  # Initialize variable to store the decrypted text
        text = input("Enter the Morse code message: ")  # Prompt user for Morse code input
        for transfercode in text.split():  # Loop through each Morse code symbol
            CODE = MORSE_CODE_DICT2.get(transfercode)  # Get the corresponding letter for the Morse code
            PLAINTEXT += CODE  # Add the letter to the decrypted text
        print("Decrypted Plaintext:", PLAINTEXT)  # Print the decrypted text

    elif choice == '3':  # If the user chooses to exit
        print("Exiting the program.")  # Print exit message
        break  # Exit the loop and terminate the program

    else:  # If the input is invalid
        print("Please choose again.")  # Print message prompting the user to choose again
