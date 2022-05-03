#introducao_pacman.py
import pygame

#Constantes
LARGURA=1900 #x
ALTURA=1000 #y
TELA=(LARGURA,ALTURA) #ou [LARGURA,ALTURA]
PRETO=(0,0,0)
BRANCO=(255,255,255)
AMARELO=(255,255,0)
VELOCIDADE=0.1
raio=30

#Cria a tela gráfica
tela=pygame.display.set_mode(TELA,0)
#Titulo da tela
pygame.display.set_caption('Game com Python')

x=10
y=10
vel_x=VELOCIDADE
vel_y=VELOCIDADE

#loop do jogo
while True:

    #Calcula as regras do jogo
    x+=vel_x
    y+=vel_y


    if x+raio>LARGURA:
        vel_x=-VELOCIDADE
    elif x-raio<0:
        vel_x=+VELOCIDADE
        
    if y+raio>ALTURA:
        vel_y=-VELOCIDADE
    elif y-raio<0:
        vel_y=+VELOCIDADE
        
    local=x,y
    
    #pinta a tela
    tela.fill(PRETO)

    #desenha um circulo preenchido
    pygame.draw.circle(tela,BRANCO,local,raio,0)
    pygame.display.update()

    #Processa os eventos do pygame
    #pega cada evento do pygame e salva na variável "e"
    for e in pygame.event.get():
        #se o tipo de evento == SAIR (clicou X)
        if e.type==pygame.QUIT:
            exit() #fecha o pygame
