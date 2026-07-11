from art import art_higher_lower, art_versus
from game_data import data
import random

def display_art_higher_lower() -> None:
    print(art_higher_lower)


def display_art_versus() -> None:
    print(art_versus)


def display_first_celebrity_summary(data: list[dict], index: int) -> None:
    print(f"Compare A: {data[index]["name"]}, a {data[index]["description"]}, from {data[index]["country"]}.")


def display_second_celebrity_summary(data: list[dict], index: int) -> None:
    print(f"Against B: {data[index]["name"]}, a {data[index]["description"]}, from {data[index]["country"]}.")


def display_question() -> str:
    while True:
        response = input("Who has more followers? Type 'A' or 'B': " ).upper()
        if response in ("A", "B"):
            return response


def generate_random_index() -> int:
    return random.randint(0,len(data)-1)


def generate_structure_orchestration() -> list[int]:
    while True:
        random_index = [generate_random_index(), generate_random_index()]
        if random_index[0] != random_index[1]:
            return random_index


def outcome(data: list, random_index: list) -> int:
    first_score = data[random_index[0]]['follower_count']
    second_score = data[random_index[1]]['follower_count']

    if first_score > second_score:
        return random_index[0]
    else:
        return random_index[1]


def generate_different_index(index_to_avoid: int) -> int:
    while True:
        new_index = generate_random_index()

        if new_index != index_to_avoid:
            return new_index


def final_score(score: int) -> None:
    print(f"Sorry, that's wrong. Final score: {score}.")


def intermediate_score(score: int) -> None:
    print(f"\nYou're right! Current score: {score}.\n")


def run_higher_lower():
    score = 0
    display_art_higher_lower()
    random_index = generate_structure_orchestration()

    while True:
        display_first_celebrity_summary(data, random_index[0])
        display_art_versus()
        display_second_celebrity_summary(data, random_index[1])

        response = display_question()
        result = outcome(data, random_index)

        if response == "A":
            selected_index = random_index[0]
        elif response == "B":
            selected_index = random_index[1]

        if selected_index == result:
            score += 1
            intermediate_score(score)

            random_index[0] = result
            random_index[1] = generate_different_index(random_index[0])


        else:
            break

    final_score(score)





run_higher_lower()
