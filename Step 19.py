import library as lib

think(10)
put()
move()
while not object_here("banana"):
    if right_is_clear():
        lib.turn_right()
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