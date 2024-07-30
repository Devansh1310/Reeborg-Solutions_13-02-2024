import library as lib 

think(10)
while not is_facing_north():
    turn_left()
while front_is_clear():
    move()
turn_left()
repeat 3:
    while not wall_in_front():
        move()
    turn_left()
    
lib.farm()

lib.put_back()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    repeat 3:
        turn_left()

def turn_right():
    repeat 3:
        turn_left()

def farm():
    while not at_goal():
        while object_here("carrot"):
            take()
        if not object_here():
            move()
        if wall_in_front() and is_facing_north():
            while object_here("carrot"):
                take()
            turn_left()
            if front_is_clear():
                move()
            turn_left()
        if wall_in_front() and not is_facing_north():
            while object_here("carrot"):
                take()
            turn_right()
            if front_is_clear():
                move()
            turn_right()

def put_back():
    while not is_facing_north():
        turn_left()
    while front_is_clear():
        while object_here("carrot"):
            take()
        if not object_here():
            move()
    if wall_in_front():
        while object_here("carrot"):
                take()
        turn_right()
    while front_is_clear():
        move()
    if wall_in_front():
        while carries_object():
            put()
    repeat 2:
        turn_left()
    while front_is_clear():
        move()
    if wall_in_front():
        turn_left()
    while not at_goal():
        move()
    