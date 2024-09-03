import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

input_letter = int(input("How many letters would you like in your password?\n"))
input_symbol = int(input("How many symbols would you like in your password?\n"))
input_number = int(input("How many numbers would you like in your password?\n"))

random.shuffle(letter)
random.shuffle(symbol)
random.shuffle(number)

selected_letter = letter[:input_letter]
selected_symbol = letter[:input_symbol]
selected_number = letter[:input_number]

combined_shuffle = selected_letter + selected_symbol + selected_number

random.shuffle(combined_shuffle)

password = ''.join(combined_shuffle)

print(f"Here's your password: {password}")



