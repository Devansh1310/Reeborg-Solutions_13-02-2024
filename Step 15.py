import library as lib

think(10)
move()
lib.turn_right()
move()
while front_is_clear() and not at_goal():
    move()
    if wall_in_front():
        turn_left()
    elif not wall_on_right():
        lib.turn_right()
        build_wall()
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    repeat 3:
        turn_left()