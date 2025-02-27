import pygame
from pygame.locals import * #submodolo
from sys import exit
import random

pygame.init() #inicializar as funcoes e variaveis do pygame

largura = 1920/2
altura = 1080/2
local_objeto = 200,300
x = largura/2
y = 0
cor = 255,0,0

tela = pygame.display.set_mode((largura,altura)) #largura e altura da tela
pygame.display.set_caption('Tetris')
while True: #loop
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
           x = x - 1
        if event.key == K_RIGHT:
           x = x + 1
        if event.key == K_UP:
           y = y - 1 
        if event.key == K_DOWN:
           y = y + 1

    #cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    
    #-----------------------------X---Y---L--A)
    pygame.draw.rect(tela,(cor),(x,y,50,100))
    if y >= altura:
        y = 0
    y = y + 2/5

    #x = x + 1
    #pygame.draw.rect(tela,(cor),(200,300,100,5))#Reta esquerda
    #pygame.draw.rect(tela,(cor),(300,300,5,100))#Reta esquerda
    #pygame.draw.rect(tela,(cor),(200,300,5,100))#Teto
    #pygame.draw.rect(tela,(cor),(200,400,100,5))#Chao

    pygame.display.update()
    
    #organizador de estoque,saida e entrada de carga de caminhoes