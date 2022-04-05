#jogo_da_forca.py
                #012345
palavra_secreta='BARATO'
tamanho=len(palavra_secreta) #6
acertos=0
ja_foi=[] #lista vazia que vai guardar letras chutadas
#                 0        1           2                 3                4              5
partes_corpo=['cabeça','tronco','perna esquerda','perna direita','braço esquerdo','braço direito']
digitadas=[]


def mostrar_digitadas():
    print('Palavra secreta: ',end='')
    for item in digitadas:
        print(item,end=' ')
        
def salvar_letra(letra):
    ind = 0
    encontrou = 0
    for c in palavra_secreta:
        if c == letra:
            encontrou += 1
            digitadas[ind]=letra
        ind += 1
    return encontrou


print('\n\n\t\t\t##################################')
print('\t\t\t##  Bem vindo ao jogo da forca  ##')
print('\t\t\t##################################')

for letra in palavra_secreta:
    print('__',end='  ')               #  0   1   2   3   4   5
    digitadas.append('__') #digitadas = ['__''__''__''__''__''__']
print()

while True:
    letra=input('\nDigite uma letra: ').upper()


    if len(letra)==0:
        continue

    if letra in ja_foi:
        print('\nJá foi digitada! Tente outra!')
        continue

    #salva cada letra digitada

    if letra in palavra_secreta:
        print('\nAcertou. Muito bem!')
        acertos += salvar_letra(letra)
        mostrar_digitadas()

        if acertos==tamanho:
            print('\nVocê venceu! Parabéns!!!')
            break

    else:
        print('Errou! hehehe. Enforcou:',partes_corpo[0])
        del partes_corpo[0]
        if len(partes_corpo)==0:
            print('\nVocê perdeu! hahahaha')
            break




























