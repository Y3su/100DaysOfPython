# Import the 'string' module which provides a collection of string-related functions and constants
import string

# Import 'logo' from a module named 'caesar_cipher_art'.
# Presumably, 'logo' is a predefined variable or string (like an ASCII art logo).
from caesar_cipher_art import logo

# Print the 'logo' (ASCII art) to the console.
print(logo)

# Generate a list of lowercase alphabet letters from 'a' to 'z'.
alphabet = list(string.ascii_lowercase)


# Define a function 'caesar' that takes three arguments:
# 'original_text' - the input text,
# 'shift_amount' - how much to shift each letter,
# 'encode_or_decode' - specifies whether to 'encode' (encrypt) or 'decode' (decrypt).
def caesar(original_text, shift_amount, encode_or_decode):
    # Initialize an empty string to hold the final encoded/decoded result
    cipher_text = ""

    # If the user wants to 'decode', reverse the shift direction (negative shift)
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each letter in the 'original_text'
    for letter in original_text:

        # If the letter is not in the alphabet (e.g., spaces or punctuation), add it directly to the result
        if letter not in alphabet:
            cipher_text += letter

        # If the letter is in the alphabet, perform the Caesar Cipher shifting
        else:
            # Find the position of the letter in the alphabet and apply the shift
            shifted_position = alphabet.index(letter) + shift_amount
            # Use modulo to wrap around if the position exceeds the alphabet length
            shifted_position %= len(alphabet)
            # Add the shifted letter to the result
            cipher_text += alphabet[shifted_position]

    # After looping through all letters, print the final encoded/decoded result
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


# Set a variable 'start' to True to begin a loop that will repeatedly ask for user input
start = True

# Start a loop that continues as long as 'start' is True
while start:

    # Ask the user if they want to encode (encrypt) or decode (decrypt) and store their input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

    # Ask the user to input the message they want to process and convert it to lowercase
    text = input("Type your message:\n").lower()

    # Ask the user to input the shift number and convert it to an integer
    shift = int(input("Type the shift number: \n"))

    # Call the 'caesar' function with the user's input: original text, shift amount, and direction
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to continue using the program
    should_continue = input("Do you want to continue? [Yes] [No]\n").lower()

    # If the user wants to continue, set 'start' to True (the loop will repeat)
    if should_continue == "yes":
        start = True

    # If the user doesn't want to continue, print "Goodbye" and exit the loop by setting 'start' to False
    elif should_continue == "no":
        print("Goodbye")
        start = False
