def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_bump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    


while at_goal()==False:
    if front_is_clear():
        move()
    else:
        one_bump()