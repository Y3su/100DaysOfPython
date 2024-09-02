import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

game_image = [rock, scissors, paper]

choice_input = input("What do you choose? Type 0 for Rock, Type 1 for Scissors, Type 2 for Paper\n")

if choice_input.isdigit():
    choice = int(choice_input)
    if choice in [0, 1, 2]:
        print(game_image[choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose: ")
        print(game_image[computer_choice])

        if choice == 0 and computer_choice == 2:
            print("Computer wins")
        elif choice == 0 and computer_choice == 1:
            print("You win!")
        elif choice == 1 and computer_choice == 0:
            print("Computer wins")
        elif choice == 1 and computer_choice == 2:
            print("You win!")
        elif choice == 2 and computer_choice == 0:
            print("You win!")
        elif choice == 2 and computer_choice == 1:
            print("Computer wins")
        elif choice == computer_choice:
            print("It's a Draw!")
    else:
        print("Invalid input. Please enter 0, 1, or 2")
else:
    print("Invalid input. Please enter a number")