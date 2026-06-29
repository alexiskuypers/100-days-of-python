import random
from game_art import rock, paper, scissors

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game_images = [rock, paper, scissors]

computer_choice = random.randint(0,2)


if user_choice not in (0,1,2):
    print(f"{user_choice} is an incorrect values")
    SystemExit()


print(game_images[user_choice])
print("\n\ncomputer chose:\n" + game_images[computer_choice] + "\n")


if user_choice == 0 and computer_choice == 2 :
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
elif user_choice < computer_choice or user_choice == 2 and computer_choice == 0:
    print("You lose!")
else:
    print("you win!")
