import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
letters_input = int(input("How many letters would you like in your password?"))
symbols_input = int(input("How many symbols would you like?"))
numbers_input = int(input("How many numbers would you like?"))


password = ""

for char in range(1,(letters_input + 1)):
    password += random.choice(letters)

for char in range(1,(numbers_input + 1)):
    password += random.choice(numbers)

for char in range(1,(symbols_input + 1)):
    password += random.choice(symbols)


final_password = "".join(random.sample(password, len(password)))

print(final_password)














"Your password is: "
