import library as lib

think(10)

lib.get_apples()

lib.put_apples()

lib.get_back_to_ckeckpoint()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    repeat 3:
        turn_left()

def get_apples():
    turn_left()
    repeat 2:
        move()
    turn_right()
    move()
    while object_here("apple"):
        take()

def put_apples():
    turn_right()
    repeat 3:
        move()
    turn_left()
    repeat 4:
        move()
    turn_left()
    repeat 4:
        move()
    while carries_object("apple"):
        put()
        
def get_back_to_ckeckpoint():
    repeat 2:
        turn_left()
    repeat 4:
        move()
    turn_right()
    repeat 5:
        move()
    turn_left()
    repeat 2:
        move()