import pygame, math


# This function will test the collision of any two sprites you put into it
def isCollision(object1_X, object1_Y, object2_X, object2_Y):
    distance = math.sqrt(math.pow(object1_X - object2_X, 2) + (math.pow(object1_Y - object2_Y, 2)))
    if distance < 27: 
        return True
    else:
        return False

# This function will allow you to display a score just pass it the location of where 
# you would like the scores displayed and what the score is
def show_score(x, y, score_value):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Moving your sprites
#def move_Horizontal(object1_X, object1_Y, move):