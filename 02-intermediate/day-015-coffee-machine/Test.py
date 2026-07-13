


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 2000,
    "coffee": 155,
}


def substract_resources(content: str, MENU: dict, resources: dict):
    ingredients_to_substact = MENU[content]["ingredients"]

    for ingredient, value in resources.items():
        if ingredients_to_substact.get(ingredient) is not None:
            value = value - ingredients_to_substact.get(ingredient)
        resources[ingredient] = value

    return resources


print(substract_resources("espresso", MENU, resources=resources))
