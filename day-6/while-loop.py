def turn_right()
    turn_left()
    turn_left()
    turn_left()

def one_bump()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False
    one_bump()
    
#while at_goal() != True
#    one_bump()
    
#while not at_goal()
#    one_bump()