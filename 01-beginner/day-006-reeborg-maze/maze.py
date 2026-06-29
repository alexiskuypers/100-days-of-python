# pyright: reportUndefinedVariable=false


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    else :
        while front_is_clear() and wall_on_right():
            move()
