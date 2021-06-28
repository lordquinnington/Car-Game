#~~~~~ car game title screen ~~~~~#

import pygame
from random import randint

def titleScreen(score):
    pygame.init()
    display = pygame.display.set_mode((800,600))
    pygame.display.set_caption("A bit racey")

    white = (255,255,255)
    red = (255,0,0)
    lightRed = (210,0,0)
    lightRed2 = (250,0,0)
    black = (0,0,0)

    text = pygame.font.SysFont('curlz',80)
    text2 = pygame.font.SysFont('curlz',50)
    text3 = pygame.font.SysFont('arial',45)
    playing = True
    playGame = False

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        display.fill(white)
        mouse_position = pygame.mouse.get_pos()

        display.blit(text.render("A Bit Racey",False,red),(220,140))
        display.blit(text2.render("Score: "+str(score),False,red),(290,245))

        pygame.draw.rect(display,lightRed,(200,340,170,70))

        if 200 < mouse_position[0] < 370 and 340 < mouse_position[1] < 410:
            pygame.draw.rect(display,lightRed2,(200,340,170,70))

            if event.type == pygame.MOUSEBUTTONDOWN:
                playGame = True
                playing = False

        display.blit(text3.render("Play",False,black),(247,348))


        pygame.draw.rect(display,lightRed,(400,340,170,70))

        if 400 < mouse_position[0] < 570 and 340 < mouse_position[1] < 410:
            pygame.draw.rect(display,lightRed2,(400,340,170,70))

            if event.type == pygame.MOUSEBUTTONDOWN:
                playing = False

        display.blit(text3.render("Quit",False,black),(447,348))


        pygame.display.flip()

    pygame.quit()

    if playGame:
        carGame()

def carGame():
    pygame.init()
    display = pygame.display.set_mode((600,600))
    pygame.display.set_caption("A bit racey")

    car = pygame.image.load("Car2.PNG")
    car = pygame.transform.scale(car,(50,100))
    obstacle = pygame.image.load("Obstacle.PNG")
    obstacle = pygame.transform.scale(obstacle,(50,100))

    score = 0
    carXPos = 275
    currentObstacles = []
    white = (255,255,255)
    black = (0,0,0)
    count = 0
    show = 400
    text = pygame.font.SysFont('arial',30)
    goLeft = False
    goRight = False
    playing = True
    goToTitleScreen = False

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not goLeft:
                        goLeft = True

                if event.key == pygame.K_RIGHT:
                    if not goRight:
                        goRight = True

                if event.key == pygame.K_ESCAPE:
                    playing = False
                    goToTitleScreen = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if goLeft:
                        goLeft = False

                if event.key == pygame.K_RIGHT:
                    if goRight:
                        goRight = False

        mouse_position = pygame.mouse.get_pos()
        display.fill(white)

        display.blit(text.render("Score: "+str(score),False,black),(5,0))

        if goLeft:
            if carXPos > 5:
                carXPos -= 1
            else:
                goLeft = False

        if goRight:
            if carXPos < 545:
                carXPos += 1
            else:
                goRight = False
                
        display.blit(car,(carXPos,485))

        if count == show:
            currentObstacles.append([randint(5,545),-100])
            count = 0
        else:
            count += 1

        belowScreen = []
        for item in currentObstacles:
            item[1] += 1
            if carXPos <= item[0] <= (carXPos + 50) or carXPos <= (item[0] + 50) <= (carXPos + 50):
                if 485 <= item[1] <= 585 or 485 <= (item[1] + 100) <= 585:
                    playing = False
                    goToTitleScreen = True
            if item[1] > 600:
                belowScreen.append(item)
                score += 1
            display.blit(obstacle,(item[0],item[1]))

            

        for image in belowScreen:
            currentObstacles.remove(image)

        pygame.display.flip()

    pygame.quit()

    if goToTitleScreen:
        titleScreen(score)

titleScreen(0)
