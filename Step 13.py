import library as lib

think(10)
while not at_goal():
    if front_is_clear():
        move()
    else:
        lib.hurdle_jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def hurdle_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    repeat 3:
        turn_left()