from data import MENU, resources


#input fonction
def get_user_selection() -> str:
    while True:
        result = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if result in ("espresso", "latte", "cappuccino", "off", "report"):
            return result


#fonction that will manage the financial side
def ask_for_money() -> dict:
    print("Please insert coins.")
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

        except ValueError:
            print("Please enter integer")
            continue
        else:
            flag = False
            all_currency = [quarters, dimes, nickels, pennies]
            for amount in all_currency:
                if amount < 0:
                    flag = True
                    print("Coin amounts cannot be negative.")
            if not flag:
                break

    return {
        "quarters": quarters,
        "dimes": dimes,
        "nickels": nickels,
        "pennies": pennies,
    }


def calculate_total_amount(amount_by_currency: dict) -> float:
    total_amount = 0
    for currency, amount in amount_by_currency.items():

        if currency == "quarters":
            amount *= 0.25

        if currency == "dimes":
            amount *= 0.10

        if currency == "nickels":
            amount *= 0.05

        if currency == "pennies":
            amount *= 0.01

        total_amount += amount

    return float(total_amount)


def get_price(menu: dict, content: str) -> float:
    return menu[content]["cost"]


#Fonction that will manage resources
def validate_resources(content: str, menu: dict, resources: dict) -> dict:
    required_ingredients = menu[content]["ingredients"]
    missing_resources = {}

    for ingredient, required_value in required_ingredients.items():
        available_resource = resources[ingredient]

        if available_resource < required_value:
            missing_resources[ingredient] = required_value - available_resource

    return missing_resources


def subtract_resources(content: str, menu: dict, resources: dict) -> None:
    ingredients_to_subtract = menu[content]["ingredients"]

    for ingredient, value in resources.items():
        if ingredients_to_subtract.get(ingredient) is not None:
            value = value - ingredients_to_subtract.get(ingredient)
        resources[ingredient] = value

    return None


#Fonction that will display a result to user
def display_result_transaction(inserted_amount: float, menu: dict, content: str) -> None:
    price = menu[content]["cost"]

    if inserted_amount < price:
        inserted_amount = abs(round(inserted_amount,2))
        print("Sorry that's not enough money. Money refunded.")

    elif inserted_amount >= price:
        print(f"Here is ${round(inserted_amount - price, 2)} dollars in change.")


def display_resource(resource: dict, amount_won: float) -> None:
    print(f"Water: {resource["water"]}\n"
          f"Milk: {resource["milk"]}\n"
          f"Coffee:{resource["coffee"]}\n"
          f"Money won: {round(amount_won,2)}$"
        )


def display_missing_resources(missing_resource: dict) -> None:
    for ingredient, value in missing_resource.items():

        if ingredient in ("water", "milk"):
            print(f"Sorry there is not enough {ingredient}, {value}ml is needed")

        elif ingredient == "coffee":
            print(f" “Sorry there is not enough {ingredient}, {value}g is needed")


def print_end_message(content: str) -> None:
    print(f"“Here is your {content}. Enjoy!”")


#orchestration fonction
def run_coffee_machine() -> None:
    amount_won = 0

    while True:
        content = get_user_selection()
        if content == "off":
            return

        elif content == "report":
            display_resource(resources, amount_won)
            continue

        current_resources = validate_resources(content, MENU, resources)

        if current_resources:
            display_missing_resources(current_resources)
            continue

        inserted_amount = calculate_total_amount(ask_for_money())
        price = get_price(MENU, content)

        if inserted_amount >= price:
            display_result_transaction(inserted_amount, MENU, content)
            amount_won += price
            subtract_resources(content, MENU, resources)
            print_end_message(content)

        else:
            display_result_transaction(inserted_amount, MENU, content)


if __name__=="__main__":
    run_coffee_machine()






