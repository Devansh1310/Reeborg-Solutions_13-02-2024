from library import jump_hurdle, turn_right

think(10)
while not at_goal():
    jump_hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    repeat 3:
        turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()