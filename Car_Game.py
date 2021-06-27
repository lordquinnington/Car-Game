#~~~~~ car game ~~~~~#

import pygame
from random import randint

isButtonPressed = False
beingPressed = False

class Obstacle:
    def __init__(self,pDisplay,pXPos):
        width, self._height = pygame.display.get_surface().get_size()
        x = randint(1,2)
        y = pygame.image.load("Child"+str(x)+".PNG")
        self._imgW = round((width) * 0.07)
        self._imgH = round((self._height) * 0.20)
        self._img = pygame.transform.scale(y,(self._imgW,self._imgH))
        
        self._display = pDisplay
        self._xPos = pXPos
        self._yPos = 0 - self._imgH

    def moveDown(self):
        self._yPos += 1

    def render(self):
        self._display.blit(self._img,(self._xPos,self._yPos))

    def hasCollided(self,pCarXPos,pCarYPos,pCarW,pCarH):
        if pCarXPos <= self._xPos <= (pCarXPos + pCarW) or pCarXPos <= (self._xPos + self._imgW) <= (pCarXPos + pCarW):
            if pCarYPos <= self._yPos <= (pCarYPos + pCarH) or pCarYPos <= (self._yPos + self._imgH) <= (pCarYPos + pCarH):
                return True

        return False

    def needToDelete(self):
        if self._yPos > self._height:
            return True

        return False
        

def button(display,mousePos,colour1,colour2,colour3,x_posBut,y_posBut,height,width,borderRadius,font,text,textColour,x_posText,y_posText):
    global isButtonPressed
    global beingPressed
    
    pygame.draw.rect(display,(colour1),(x_posBut,y_posBut,width,height),border_radius=borderRadius)
    
    if (x_posBut) < mousePos[0] < (x_posBut+width) and (y_posBut) < mousePos[1] < (y_posBut+height):
        pygame.draw.rect(display,(colour2),(x_posBut,y_posBut,width,height),border_radius=borderRadius)
        
        if event.type == pygame.MOUSEBUTTONDOWN and not isButtonPressed:
            isButtonPressed = True
            beingPressed = True
            
        elif event.type == pygame.MOUSEBUTTONUP:
            isButtonPressed = False
            beingPressed = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(display,(colour3),(x_posBut,y_posBut,width,height),border_radius=borderRadius)
            beingPressed = False

    display.blit(font.render(text,False,textColour),(x_posText,y_posText))
    return beingPressed

pygame.init()
display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Car Game")

width, height = pygame.display.get_surface().get_size()

car = pygame.image.load("Car.PNG")
carWidth = round((width) * 0.09)
carHeight = round((height) * 0.24)
car = pygame.transform.scale(car,(carWidth,carHeight))
score = 0
car_x_pos = (width // 2) - (carWidth // 2)
car_y_pos = height - (carHeight + 25)

appear = 0
appearAfter = 500
obstacles = []

font1 = pygame.font.SysFont('verdana',27)

running = True
moveRight = False
moveLeft = False
moveUp = False
moveDown = False
collided = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if not moveRight:
                    moveRight = True

            if event.key == pygame.K_LEFT:
                if not moveLeft:
                    moveLeft = True

            if event.key == pygame.K_UP:
                if not moveUp:
                    moveUp = True

            if event.key == pygame.K_DOWN:
                if not moveDown:
                    moveDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if moveRight:
                    moveRight = False

            if event.key == pygame.K_LEFT:
                if moveLeft:
                    moveLeft = False

            if event.key == pygame.K_UP:
                if moveUp:
                    moveUp = False

            if event.key == pygame.K_DOWN:
                if moveDown:
                    moveDown = False

    mousePos = pygame.mouse.get_pos()
    display.fill((255,255,255))

    ################################ top items ################################

    if button(display,mousePos,(65,150,240),(95,170,255),(6,140,225),15,15,40,90,2,font1,"Quit",(20,20,20),31,16):
        running = False

    display.blit(font1.render("SCORE: "+str(score),False,(20,20,20)),(120,15))

    ################################ moving the car ################################

    if moveLeft:
        if car_x_pos > 15:
            car_x_pos -= 2
        else:
            moveLeft = False

    if moveRight:
        if car_x_pos < width - 15 - carWidth:
            car_x_pos += 2
        else:
            moveRight = False

    if moveUp:
        if car_y_pos > 70:
            car_y_pos -= 1
        else:
            moveUp = False

    if moveDown:
        if car_y_pos < height - 15 - carHeight:
            car_y_pos += 1
        else:
            moveDown = False

    ################################ making objects appear ################################

    if appear == appearAfter:
        obstacles.append(Obstacle(display,randint(15,width-15)))
        appear = 0

    else:
        appear += 1

    delete = []
    for obstacle in obstacles:
        obstacle.render()
        obstacle.moveDown()
        if obstacle.hasCollided(car_x_pos,car_y_pos,carWidth,carHeight):
            collided = True
            running = False
        if obstacle.needToDelete():
            delete.append(obstacle)
            score += 1

    for toDelete in delete:
        obstacles.remove(toDelete)
        

    display.blit(car,(car_x_pos,car_y_pos))

    pygame.display.flip()

pygame.quit()

