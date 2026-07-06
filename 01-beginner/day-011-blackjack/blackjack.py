import random
from art import black_jack_art


cards = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
]

player_cards = []
computer_cards = []


def ask_to_play() -> str:
    while True:
        play_new_game = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': "
        )

        if play_new_game in ("y", "n"):
            return play_new_game


def ask_to_draw() -> str:
    while True:
        draw = input(
            "Type 'y' to get another card, type 'n' to pass: "
        )

        if draw in ("y", "n"):
            return draw


def ask_to_restart() -> str:
    while True:
        restart = input(
            "Do you want to play another game of Blackjack? "
            "Type 'y' or 'n': "
        )

        if restart in ("y", "n"):
            return restart


def sum_cards(list_of_cards: list[int]) -> int:
    total = sum(list_of_cards)

    if 1 in list_of_cards and total + 10 <= 21:
        total += 10

    return total


def select_cards() -> None:
    random_player_cards = random.choices(cards, k=2)
    random_computer_cards = random.choices(cards, k=2)

    player_cards.extend(random_player_cards)
    computer_cards.extend(random_computer_cards)


def to_draw() -> int:
    card = random.choice(cards)
    return card


def computer_draw(total_computer_hand: int) -> str:
    if total_computer_hand < 17:
        return "y"

    return "n"


def reset(player_hand: list[int], computer_hand: list[int]) -> None:
    player_hand.clear()
    computer_hand.clear()


def art_first_game() -> None:
    print(black_jack_art)


def display_game_state(
    player_hand: list[int],
    total_player_hand: int,
    computer_hand: list[int],
) -> None:
    print(
        f"Your cards: {player_hand}, "
        f"current score: [{total_player_hand}]\n"
        f"Computer's first card: {computer_hand[0]}"
    )


def display_game_state_computer(
    player_hand: list[int],
    computer_hand: list[int],
    total_player_hand: int,
    total_computer_hand: int,
) -> None:
    print(
        f"Your final hand: {player_hand}, "
        f"final score: {total_player_hand}\n"
        f"Computer's final hand: {computer_hand}, "
        f"final score: {total_computer_hand}"
    )


def result_output(
    total_player_hand: int,
    total_computer_hand: int,
) -> None:
    if total_player_hand > 21:
        print("You went over. You lose 😭")

    elif total_computer_hand > 21:
        print("Opponent went over. You win 😁")

    elif total_player_hand == total_computer_hand:
        print("It's a draw!")

    elif total_player_hand == 21:
        print("Win with a Blackjack 😎")

    elif total_player_hand > total_computer_hand:
        print("You win 😃")

    else:
        print("You lose 😤")


def run_blackjack() -> None:
    select_cards()

    total_player_hand = sum_cards(player_cards)
    total_computer_hand = sum_cards(computer_cards)

    display_game_state(
        player_cards,
        total_player_hand,
        computer_cards,
    )

    while total_player_hand < 21:
        draw = ask_to_draw()

        if draw == "y":
            card = to_draw()
            player_cards.append(card)

            total_player_hand = sum_cards(player_cards)

            display_game_state(
                player_cards,
                total_player_hand,
                computer_cards,
            )
        else:
            break

    if total_player_hand > 21:
        display_game_state_computer(
            player_cards,
            computer_cards,
            total_player_hand,
            total_computer_hand,
        )

        result_output(
            total_player_hand,
            total_computer_hand,
        )

        reset(player_cards, computer_cards)
        return

    while computer_draw(total_computer_hand) == "y":
        card = to_draw()
        computer_cards.append(card)

        total_computer_hand = sum_cards(computer_cards)

    display_game_state_computer(
        player_cards,
        computer_cards,
        total_player_hand,
        total_computer_hand,
    )

    result_output(
        total_player_hand,
        total_computer_hand,
    )

    reset(player_cards, computer_cards)


def main() -> None:
    play_new_game = ask_to_play()

    while play_new_game == "y":
        art_first_game()
        run_blackjack()
        play_new_game = ask_to_restart()


main()
