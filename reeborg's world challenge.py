def turn_right():
    turn_left()
    turn_left()
    turn_left()


def corner_left():
    move()
    turn_left()
    move()


def corner_right():
    move()
    turn_right()
    move()


for step in range(6):
    corner_left()
    turn_right()
    corner_right()
    turn_left()

# Go to the following website and copy/paste the code:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Using a while loop with a for loop to complete the third hurdle
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def corner_left():
    turn_left()
    move()


def corner_right():
    move()
    turn_right()
    move()


while not at_goal():
    if wall_in_front():
        corner_left()
        turn_right()
        corner_right()
        turn_left()
    else:
        move()

# hurdle, 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def corner_right():
    turn_right()
    move()


while not at_goal():
    if wall_in_front():
        if right_is_clear():
            corner_right()
        else:
            turn_left()
    elif right_is_clear():
        corner_right()
    else:
        move()

# Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def corner_right():
    turn_right()
    move()


while not at_goal():
    if wall_in_front():
        if right_is_clear():
            corner_right()
        else:
            turn_left()
    elif right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        corner_right()
    else:
        move()