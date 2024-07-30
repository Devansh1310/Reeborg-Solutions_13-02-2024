from library import taking_all, putting_all

#so the program works fater
think(10)

taking_all() 

#turn into the opposite direction 
repeat 2:
    turn_left()   

#move back to the checkpoint
repeat 12:
    move()
 
putting_all()

move()  

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
#the fuction takes the object when present using if and elif
def taking_all():
    repeat 13:
        if object_here("dandelion"):
            take()
            move()
        elif front_is_clear():
            move()

#the function puts all the objects 
def putting_all():
    repeat 13:
        if carries_object("dandelion"):
            put()