import pygame, math


# This function will test the collision of any two sprites you put into it
def isCollision(object1_X, object1_Y, object2_X, object2_Y):
    distance = math.sqrt(math.pow(object1_X - object2_X, 2) + (math.pow(object1_Y - object2_Y, 2)))
    if distance < 27: # This is not finished
        return True
    else:
        return False

# This function will allow you to display a score just pass it the location of where 
# you would like the scores displayed and what the score is