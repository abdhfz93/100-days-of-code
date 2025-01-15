def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_bump():
    turn_left()
    while wall_on_right()== True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_in_front()== False:
        move()
    turn_left()


while at_goal()==False:
    if front_is_clear():
        move()
    else:
        one_bump()