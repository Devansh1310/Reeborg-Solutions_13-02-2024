from library import taking_all, putting_all

think(10)
taking_all() 
repeat 2:
    turn_left()   
repeat 12:
    move()
putting_all()
move()  

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def taking_all():
    repeat 13:
        if object_here("dandelion"):
            take()
            move()
        elif front_is_clear():
            move()

def putting_all():
    repeat 13:
        if carries_object("dandelion"):
            put()