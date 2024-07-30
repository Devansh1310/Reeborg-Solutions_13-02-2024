def left():
    move()
    turn_left()
    move()
    take()
    move()
    take()
    repeat 2:
        turn_left()
    repeat 2:
        move()
    put()
    put()
    turn_left()
def right():
    move()
    repeat 3:
        turn_left()
    move()
    take()
    move()
    take()
    repeat 2:
        turn_left()
    move()
    move()
    put()
    put()
    repeat 3:
        turn_left()
left()   
right()
left()
right()
repeat 2:
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
