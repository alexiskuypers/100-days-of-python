import random

from gameart import stages


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
blank_word = "_" * len(chosen_word)

print(f"Word to guess: {blank_word}\n")

lives = 6
correct_letters = []
incorrect_letters = []
game_over = False

while not game_over:
    guess = input("Guess a letter:\n").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in correct_letters or guess in incorrect_letters:
        print("Please enter a new letter.\n")
        continue

    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        incorrect_letters.append(guess)
        lives -= 1
        print(
            f"\nYou guessed '{guess}', which is not in the word. "
            "You lose a life.\n"
        )

    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print(stages[lives])
    print(display, "\n")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    elif lives == 0:
        game_over = True
        print("****************************YOU LOSE****************************")
        print(f"The word was: {chosen_word}")
