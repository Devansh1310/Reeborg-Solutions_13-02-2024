think(10)
repeat 23:
    if front_is_clear():
        move()
    elif object_here("tulip"):
        take()
        turn_left()
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
