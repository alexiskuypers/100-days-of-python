from art import art_secret_auction
import os


def ask_secret_auction():
    name = input(f"What is your name?:\n")
    while True:
        try:
            bid = float(input("What is your bid?: $\n"))
            break
        except ValueError:
            print("Invalid bid. Please enter a number.")
    return name, bid

def restart_choice():
    while True:
        choice = input(f"Are there any other bidders? Type 'yes or 'no'.\n").strip().lower()
        if choice in ("yes", "no"):
            break
    return choice


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")



secret_auction = {}

def construct_dict(name, bid):
     secret_auction[name] = bid
     return secret_auction


def winner_auction(secret_auction):
    max_bid = 0
    for name, bid in secret_auction.items():
        if bid > max_bid:
            max_bid = bid
            winner_name = name
    return winner_name, max_bid


def output(name, max_bid):
    print (f"The winner is {name} with a bid of ${max_bid}")


def orchestration():
    print(art_secret_auction)
    while True:
        name, bid = ask_secret_auction()
        secret_auction = construct_dict(name, bid)
        restart = restart_choice()
        if restart == "no":
            break
        clear_screen()
    name, max_bid = winner_auction(secret_auction)
    output(name, max_bid)


orchestration()
