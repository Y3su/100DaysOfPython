import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

start = True
while start:
    guess = input("Guess a letter? ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        start = False


