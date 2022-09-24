def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_hurdle():
    turn_left()
    if wall_in_front():
        turn_left()
    else:
        move()
        turn_right()
def jump():
    move()
    turn_right()
    if wall_in_front():
        turn_left()
    else:
        move()
        turn_right()
while not at_goal():
    if front_is_clear():
        jump()
    if wall_in_front():
        move_hurdle()