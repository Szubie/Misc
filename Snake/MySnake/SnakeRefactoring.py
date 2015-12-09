import pygame
import random
import SnakeClasses

#I was attempt.

pygame.init()

"""world size = 20"""
FPS = 4
fps_increment=80
fps_cap=15

size = width, height = 480, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
clock=pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)
screen.fill(black)

playerX=float(size[0]/2)
playerY=float(size[1]/2)

rectangle_width=size[0]/20
rectangle_height=size[1]/20
head= pygame.draw.rect(screen, white, (playerX,playerY,rectangle_width,rectangle_height), 0)
snake=[head]



up=0
down=1
left=2
right=3
direction=0

pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = False

running=True
while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        else:
            SnakeClasses.getKeyPress(event)
    if direction==left:
        playerX+=-size[0]/20
    if direction==right:
        playerX+=size[0]/20
    if direction==up:
        playerY+=-size[1]/20
    if direction==down:
        playerY+=size[1]/20  


    screen.fill(black)

    newX=snake[-1].x-size[0]/20
    newY=snake[-1].y-size[1]/20
    
    piece=snake[-1].copy()
    if direction==up:
        piece.y+=-size[1]/20
    elif direction==down:
        piece.y+=size[1]/20
    elif direction==left:
        piece.x+=-size[0]/20
    elif direction==right:
        piece.x+=size[0]/20
    snake.append(piece)
    
        
    snake[0].x=playerX
    snake[0].y=playerY
    
    for item in range(1,len(snake)-1):
        if snake[0].x==snake[item].x and snake[0].y==snake[item].y:
            running=False #Less sudden than pygame.quit()
    for item in snake:
        pygame.draw.rect(screen, white, (item.x, item.y, rectangle_width, rectangle_height),0)
    
    #pygame.draw.rect(screen, white, (snake[0].x, snake[0].y, rectangle_width, rectangle_height),0)
    
    clock.tick(FPS)
    pygame.display.update()
    fps_increment-=1

    if fps_increment<=0:
        if FPS<=fps_cap:
            FPS+=1
            fps_increment=80
    
    
    if playerX>size[0]-rectangle_width:
        running=False
    if playerX<0:
        running=False
    if playerY>size[1]-rectangle_height:
        running=False
    if playerY<0:
        running=False
        
        

pygame.quit()

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