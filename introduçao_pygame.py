#introduçao_pygame.py

#antes entrar na pasta SCRIPTS DO PYTHON
#pip install pygame

import pygame
import math

#Constantes gerais
#                  R, G, B
VERMELHO=(255,0, 0)
VERDE   =(0, 255,0)
AZUL    =(0,  0,255)
PRETO   =(0,  0, 0)
BRANCO  =(255,255,255)
AMARELO=(255,255,0)
LARANJA=(255,165,0)
PI=math.pi

#inicializa a biblioteca pygame
pygame.init()

#Cria a tela gráfica
tela=pygame.display.set_mode((1024,768),0)
pygame.display.set_caption('Titulo da Janela')

#pinta a tela
tela.fill(PRETO)
#                                  x  y
pygame.draw.circle(tela,VERMELHO,(50,50),50,0)
pygame.draw.circle(tela,VERMELHO,(100,50),15,1)
pygame.draw.circle(tela,VERMELHO,(150,50),20,5)

pygame.draw.line(tela,BRANCO,(450,90),(550,90),5)

pygame.draw.rect(tela,AZUL,pygame.Rect(200,30,60,30),0)
pygame.draw.rect(tela,AZUL,pygame.Rect(280,30,60,30),1)

pygame.draw.line(tela,VERMELHO,(450,20),(550,130),5)

pontos=[(50,150),(100,120),(160,140),(110,250)]
pygame.draw.polygon(tela,AMARELO,pontos,0)
pygame.draw.polygon(tela,VERMELHO,pontos,1)


#                                 retângulo                             ang inicial,final
pygame.draw.arc(tela,VERMELHO,[250,100,250,200],PI/2,   PI,  5)
pygame.draw.arc(tela,VERMELHO,[250,100,250,200],   0,   PI/2,  5)
pygame.draw.arc(tela,VERMELHO,[250,100,250,200],    3*PI/2,   2/PI,  5)
pygame.draw.arc(tela,VERMELHO,[250,100,250,200],   PI,   3*PI/2,  5)


texto="Score: {}".format(1000)
#                                                      negrito,itálico
fonte=pygame.font.SysFont("arial",48,True,False)
img_texto=fonte.render(texto,True,LARANJA)
tela.blit(img_texto,(50,350))
#atualiza a tela gráfica

pygame.display.update()
