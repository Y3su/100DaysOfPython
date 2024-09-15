import random
import hangman_art
import hangman_words

# Split the words into a list
word = hangman_words.word_list.lower().split()

# Choose a random word from the list
chosen_word = random.choice(word)

print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

start = True
correct_letters = []
lives = 6

while start:
    guess = input("Guess a letter? ").lower()

    display = ""

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            start = False
            print("You lose!")

    else:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(letter)

            elif letter in correct_letters:
                display += letter

            else:
                display += "_"

        print(display)

        if "_" not in display:
            print("You win!")
            start = False

    print(hangman_art.stages[6 - lives])

