import random

# lists
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Get user input for the lengths of letters and numbers
input_letter = int(input("How many letters would you like in your password?\n"))
input_symbol = int(input("How many symbols would you like in your password?\n"))
input_number = int(input("How many numbers would you like in your password?\n"))

# Shuffle the lists
random.shuffle(letter)
random.shuffle(symbol)
random.shuffle(number)

# Select the desired number of characters from each list
selected_letter = letter[:input_letter]
selected_symbol = symbol[:input_symbol]
selected_number = number[:input_number]

# Combine the selected characters
combined_shuffle = selected_letter + selected_symbol + selected_number

# Shuffle the combined list to mix letters and numbers
random.shuffle(combined_shuffle)

# Join the list into a single string to form the password
password = ''.join(combined_shuffle)

print(f"Here's your password: {password}")



