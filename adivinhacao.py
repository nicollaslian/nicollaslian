#adivinhacao.py

import random

total_de_tentativas=0
pontos=500


print('Qual o nível de dificuldade?')
print('(1)Muito Fácil (2)Fácil (3)Médio (4)Difícil (5)Extremo')

nivel=int(input('Defina o nível:')) #int('1') => 1

if(nivel==1):
    total_de_tentativas=20
elif(nivel==2):
    total_de_tentativas=10
elif(nivel==3):
    total_de_tentativas=5
elif(nivel==4):
    total_de_tentativas=3
else:
    total_de_tentativas=1
    


numero_secreto=random.randrange(1,101) #1,2,3,4,5...100



for tentativa in range(1,total_de_tentativas+1):

    print('Tentativa {} de {}'.format(tentativa,total_de_tentativas))

    str_chute=input('Digite um número entre 1 e 100:')
    #converte string para inteiro
    chute=int(str_chute)

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100')
        continue
    

    if chute==numero_secreto:
        print('acertou')
        break
    else:
        pontos_perdidos=abs(numero_secreto-chute)#sempre um numero sem sinal
        pontos=pontos - pontos_perdidos

        if chute>numero_secreto:
            print('Errou! seu chute foi maior que o número secreto')
        else:
            print('Errou! seu chute foi menor que o número secreto')

print('Fim do Jogo')
print('O número secreto era {}.Você fez {}'.format(numero_secreto,pontos))
