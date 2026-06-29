import sys

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choice_1 = input("You are at a crossroad, where do you want to go ? "
                 "Type 'left' or 'right'.\n").strip().lower()

if choice_1 != "left":
    print("Fall into a hole. Game Over.")
    sys.exit()


choice_2 = input("You've come to a lake. "
                 "There is an island in the middle of the lake. "
                 "Type 'wait' to wait a boat. "
                 "Type 'swim' to swim across.\n"
                ).strip().lower()

if choice_2 != "wait":
    print("Attacked by trout. Game Over.")
    sys.exit()


choice_3 = input("You arrived at the island unharmed, "
                 "there is house with 3 doors. one red, "
                 "one yellow and one blue. "
                 "Which color do you choose ?\n").strip().lower()

if choice_3 == "blue":
    print("Eaten by beasts. Game Over.")
elif choice_3 == "yellow":
    print("You Win!")
elif choice_3 == "red":
    print("Burned by fire. Game Over")
else :
    print("Game Over.")
