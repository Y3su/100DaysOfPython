# number = 0
# for adding in range (1, 101):
#     number += adding
# print(number)

# for num in range(1, 101):
#
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# input_letter = int(input("How many letters would you like in your password?\n"))
# input_symbols = int(input("How many symbols would you like in your password?\n"))
# input_numbers = int(input("How many numbers would you like in your password?\n"))

password_shuffle = [letter, number, symbol]
# random.shuffle(password_shuffle)

random.shuffle(password_shuffle)

print(password_shuffle)
# password_length = letter[:input_letter]
#
# password = ''.join(password_length)
#
# print(f"Here's your password: {password}")

