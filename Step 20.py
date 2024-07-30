import library as lib

think(100)
repeat 3:
    move()
lib.turn_right()
move()
while not at_goal():
    if right_is_clear():
        move()
        if wall_on_right():
            lib.turn_around()
            move()
            turn_left()
            build_wall()
            turn_left()
        else:
            lib.turn_around()
            move()
            turn_left()
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    repeat 3:
        turn_left()
   
def turn_around():
    repeat 2:
        turn_left()