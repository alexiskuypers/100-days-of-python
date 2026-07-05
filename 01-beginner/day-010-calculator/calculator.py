from art import art_calc


print(art_calc)


def input_ops(previous_result):
    if previous_result is not None:
        first_number = previous_result
    else:
        while True:
            try:
                first_number = float(input("What's the first number?: "))
                break
            except ValueError:
                print("Please enter a valid number.")

    while True:
        operation = input("+\n-\n*\n/\nPick an operation:\n")

        if operation in ("+", "-", "*", "/"):
            break

        print("Please enter a valid operation.")

    while True:
        try:
            second_number = float(input("What's the next number?: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    return first_number, operation, second_number


def calculation(first_number, operation, second_number):
    if operation == "+":
        return first_number + second_number

    elif operation == "-":
        return first_number - second_number

    elif operation == "*":
        return first_number * second_number

    else:
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is impossible.")

        return first_number / second_number


def output_result(first_number, operation, second_number, result):
    print(f"{first_number} {operation} {second_number} = {result}")


def start_again(result):
    while True:
        next_action = input(
            f"Type 'reuse value' to continue calculating with {result}, "
            "or type 'start over' to start a new calculation, "
            "and 'end' to stop the program: "
        ).strip().lower()

        if next_action in ("reuse value", "start over", "end"):
            break

        print("Please enter a valid action.")

    return next_action


def orchestration():
    result = None

    while True:
        first_number, operation, second_number = input_ops(result)

        try:
            new_result = calculation(
                first_number,
                operation,
                second_number
            )
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            continue

        result = new_result

        output_result(
            first_number,
            operation,
            second_number,
            result
        )

        next_action = start_again(result)

        if next_action == "reuse value":
            continue

        elif next_action == "start over":
            result = None

        else:
            return


orchestration()
