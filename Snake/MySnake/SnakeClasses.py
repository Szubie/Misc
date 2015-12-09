import random
import pygame

def spawnFood():
    xPossibleValues=[]
    x=size[0]
    while x>0:
        x-=20
        xPossibleValues.append(x)

    
    yPossibleValues=[]
    y=size[1]
    while y>0:
        y-=20
        yPossibleValues.append(y)
        
    randRoll1=random.randrange(0,len(xPossibleValues))
    randRoll2=random.randrange(0,len(yPossibleValues))
    print (randRoll1, randRoll2)
    print (xPossibleValues[randRoll1], yPossibleValues[randRoll2])
        
def getKeyPress(event):
    if event.type == pygame.KEYDOWN:          # check for key presses          
        if event.key == pygame.K_LEFT:        # left arrow turns left
            pressed_left = True
        elif event.key == pygame.K_RIGHT:     # right arrow turns right
            pressed_right = True
        elif event.key == pygame.K_UP:        # up arrow goes up
            pressed_up = True
        elif event.key == pygame.K_DOWN:     # down arrow goes down
            pressed_down = True
    elif event.type == pygame.KEYUP:            # check for key releases
        if event.key == pygame.K_LEFT:        # left arrow turns left
            pressed_left = False
        elif event.key == pygame.K_RIGHT:     # right arrow turns right
            pressed_right = False
        elif event.key == pygame.K_UP:        # up arrow goes up
            pressed_up = False
        elif event.key == pygame.K_DOWN:     # down arrow goes down
            pressed_down = False
            
    if pressed_left:
        if direction!=right:
            direction=left
    if pressed_right:
        if direction!=left:
            direction=3
    if pressed_up:
        if direction!=down:
            direction=0
    if pressed_down:
        if direction!=up:
            direction=1