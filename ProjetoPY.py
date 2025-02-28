import pygame
import Blocks
from pygame.locals import * #submodolo
from sys import exit
import random

pygame.init() #inicializar as funcoes e variaveis do pygame

LENGHT = 1920/2
WIDTH = 1080/2
x = LENGHT/2
y = 0
RED= 255,0,0
WHITE = 255,255,255
KEY_FOR_QUIT = K_ESCAPE
ITS_MOVING_LEFT = False
ITS_MOVING_RIGHT = False

def Quit():
    pygame.quit()
    exit()

def Corners():
    pygame.draw.rect(screen,(WHITE),(0,0,960,10))
    pygame.draw.rect(screen,(WHITE),(0,530,960,10))
    pygame.draw.rect(screen,(WHITE),(0,0,10,960))
    pygame.draw.rect(screen,(WHITE),(950,0,10,960)) 

screen = pygame.display.set_mode((LENGHT,WIDTH))
pygame.display.set_caption('Tetris')
while True:
    screen.fill((0,0,0))
    Corners()
    for event in pygame.event.get():
     if event.type == KEYDOWN:

        if event.key == K_LEFT and x >= 60:
            ITS_MOVING_LEFT = True

        if event.key == K_RIGHT and x <= 900:
            ITS_MOVING = True

        if event.key == K_UP:
            y = y - 1

        if event.key == K_DOWN:
            y = y + 1 

        if event.key == KEY_FOR_QUIT:
            Quit()

    if event.type == KEYUP:

        if event.key == K_LEFT:
            ITS_MOVING_LEFT = False

        if event.key == K_RIGHT:
            ITS_MOVING = False

    if ITS_MOVING_LEFT:
        x -= 1/10 
    if ITS_MOVING_RIGHT:
        x += 1/10
    #-----------------------------X---Y---L--A)
    pygame.draw.rect(screen,(RED),(x,y,50,100))
    
    if y <= 430:
        y = y + 1/5
    y == 430    

    pygame.display.update()
    
