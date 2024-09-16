import random
from hangman_art import stages, logo  # Import the hangman stages and logo from external files
from hangman_words import word_list  # Import a list of possible words to choose from

# Prints the hangman game logo
print(logo)

# Convert the word list to lowercase and split it into individual words (assuming word_list is a string of words)
word = word_list.lower().split()

# Randomly choose a word from the list to be the answer
chosen_word = random.choice(word)

# Print the chosen word (for testing purposes, remove in the final version)
print(chosen_word)

# Create a placeholder with underscores, one for each letter in the chosen word
placeholder = ""
word_length = len(chosen_word)  # Get the length of the chosen word

# Loop through the length of the word and append underscores for each letter
for position in range(word_length):
    placeholder += "_"
print(placeholder)  # Print the initial placeholder (e.g., "_ _ _ _")

# Initialize game variables
start = True  # This flag controls the while loop for the game
correct_letters = []  # List to store the correctly guessed letters
lives = 6  # Player starts with 6 lives

# Start the game loop, which will continue until the player wins or loses
while start:
    # Create the message showing how many lives the player has left
    message = f"YOU HAVE {lives}/6 LIVES LEFT"

    # Set the width of the message box (adjustable)
    box_width = 40

    # Create the top and bottom border of the message box
    border = "=" * box_width

    # Calculate the amount of space to center the message inside the box
    padding = (box_width - len(message) - 2) // 2  # Subtract 2 for the "=" at each side

    # Print the message box with centered text
    print(border)
    print(f"= {' ' * padding}{message}{' ' * padding} =")
    print(border)

    # Ask the player to guess a letter
    guess = input("Guess a letter? ").lower()  # Convert the guess to lowercase

    # If the letter has already been guessed, inform the player
    if guess in correct_letters:
        print(f"You already guessed {guess}")

    display = ""  # Initialize the display variable to show the current state of the word

    # If the guessed letter is not in the chosen word
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1  # Decrease the player's lives by 1

        # If the player runs out of lives, the game ends
        if lives == 0:
            start = False  # Stop the game loop

            # Create the losing message
            message = f"IT WAS {chosen_word.upper()}! YOU LOSE!"

            # Set the width of the message box
            box_width = 40

            # Create the border
            border = "=" * box_width

            # Calculate the padding to center the message
            padding = (box_width - len(message) - 2) // 2

            # Print the centered losing message inside the box
            print(border)
            print(f"= {' ' * padding}{message}{' ' * padding} =")
            print(border)

    # If the guessed letter is in the chosen word
    else:
        # Loop through each letter in the chosen word
        for letter in chosen_word:
            if letter == guess:  # If the guessed letter matches the current letter
                display += letter  # Add the correct letter to the display
                correct_letters.append(letter)  # Add the letter to the list of correct guesses

            elif letter in correct_letters:  # If the letter was guessed correctly in the past
                display += letter  # Show the letter in the display

            else:
                display += "_"  # If the letter hasn't been guessed, display an underscore

        print(display)  # Show the current state of the word (e.g., "m _ l k")

        # If there are no more underscores, the player has won
        if "_" not in display:
            start = False  # Stop the game loop

            # Create the winning message
            message = f"THE CORRECT WORD IS {chosen_word.upper()}! YOU WIN!"

            # Set the width of the message box
            box_width = 40

            # Create the border
            border = "=" * box_width

            # Calculate the padding to center the message
            padding = (box_width - len(message) - 2) // 2

            # Print the centered winning message inside the box
            print(border)
            print(f"= {' ' * padding}{message}{' ' * padding} =")
            print(border)

    # Show the current hangman stage based on the number of lives left
    print(stages[6 - lives])
