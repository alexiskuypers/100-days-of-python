import random
from art import guess_art


print(guess_art)

def initial_message() -> None:
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")


def ask_mode() -> int:
    while True:
        mode = input("Choose a difficulty. Type 'easy' or 'hard':\n")
        if mode == "easy":
            return 10
        if mode == "hard":
            return 5


def ask_guess() -> int:
    while True:
        try:
            guess = int(input("Make a guess:\n"))
            if guess > 0 and guess <= 100:
                return guess
        except ValueError:
            print("enter number between 1 and 100")


def remove_life(life: int) -> int:
    return life - 1


def life_output(life: int) -> None:
    print(f"You have {life} attempts remaining to guess the number.")


def specify_direction(guess_number: int, attempt: int) -> None:
    if guess_number < attempt:
        print("Too high.\nGuess again.")
    elif guess_number > attempt:
        print("Too low.\nGuess again.")


def result_output(guess_number: int, attempt: int | None) -> None:
    if guess_number == attempt:
        print(f"You got it! The answer was {guess_number}.")
    else:
        print("You've run out of guesses.")


def replay() -> str:
    while True:
        choice = input("Do you want to replay, 'y' or 'n' ?:\n")
        if choice in ("y", "n"):
            return choice


def determine_number() -> int:
    return random.randint(1,100)


def run_guessing_game() -> str:
    initial_message()
    guess_number = determine_number()
    life = ask_mode()
    life_output(life)
    attempt = None

    while life > 0:
        attempt = ask_guess()

        if attempt == guess_number:
            break

        life = remove_life(life)

        if life == 0:
            break

        specify_direction(guess_number, attempt)
        life_output(life)

    result_output(guess_number, attempt)
    return replay()


def main() -> None:
    while True:
        choice = run_guessing_game()

        if choice == "n":
            return


main()





