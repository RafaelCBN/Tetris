import pygame
from pygame.locals import * #submodolo
from sys import exit

pygame.init() #inicializar as funcoes e variaveis do pygame

largura = 500
altura = 1000
cor = 255,0,0
tela = pygame.display.set_mode((largura,altura)) #largura e altura da tela
pygame.display.set_caption('Tetris')
while True: #loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela,(cor),(200,300,5,100))
    pygame.display.update()