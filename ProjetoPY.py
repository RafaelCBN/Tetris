import pygame
from pygame.locals import * #submodolo
from sys import exit
import random

pygame.init() #inicializar as funcoes e variaveis do pygame

largura = 500
altura = 1000
local_objeto = 200,300

tela = pygame.display.set_mode((largura,altura)) #largura e altura da tela
pygame.display.set_caption('Tetris')
while True: #loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    
    #-----------------------------X---Y---L--A)
    pygame.draw.rect(tela,(cor),(400,0,1,2000))
    #pygame.draw.rect(tela,(cor),(200,300,100,5))#Reta esquerda
    #pygame.draw.rect(tela,(cor),(300,300,5,100))#Reta esquerda
    #pygame.draw.rect(tela,(cor),(200,300,5,100))#Teto
    #pygame.draw.rect(tela,(cor),(200,400,100,5))#Chao

    pygame.display.update()