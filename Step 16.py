import library as lib
think(10)

repeat 2:
    move()
turn_left()
move()

lib.farm()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    repeat 3:
        turn_left()

def farm_a_lane():
    repeat 6:
        if object_here("carrot"):
            take()
            move()
        elif front_is_clear():
            move()
    if object_here("carrot"):
            take()
def farm():
    farm_a_lane()
    turn_right()
    move()
    turn_right()
    farm_a_lane()
    turn_left()
    move()
    turn_left()
    farm_a_lane()
    turn_right()
    move()
    turn_right()
    farm_a_lane()
    turn_left()
    move()
    turn_left()
    farm_a_lane()
    turn_right()
    move()
    turn_right()
    farm_a_lane()
    turn_left()
    move()
    turn_left()
    repeat 2:
        turn_left()
    move()
    while carries_object("carrot"):
        put()