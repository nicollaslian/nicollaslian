#frutas.py

import time


#tipos de arquivos: texto ou binário
#modo de acesso ao arquivo:
#  1. Somente leitura (read) = 'r'
#  2. Escrita (write) = 'w'
#  3. Anexar (append) = 'a'

lista=[]

def entrar_fruta():
    fruta=input('Digite o nome de uma fruta: ')
    lista.append(fruta)
    
#__________________________________________________________________________________
def salvar_frutas():
    arquivo = open('cesta_de_frutas.txt','w')
    
    for fruta in lista:
        arquivo.write(fruta + '\n')

    arquivo.close()
    print ('Lista de frutas salva')

#___________________________________________________________________________________
#recupera as frutas salvas no arquivo
def recuperar_frutas():
    arquivo = open('cesta_de_frutas.txt','r')

    lista.clear()
    for linha in arquivo:
        vetor=linha.split('\n')#remove '\n' do final da linha
        lista.append(vetor[0])
        
    arquivo.close()
    print('Lista de frutas recuperada')


#___________________________________________________________________________________
def anexar_frutas():
    arquivo = open('cesta_de_frutas.txt','r')


    for linha in arquivo:
        vetor=linha.split('\n')#remove '\n' do final da linha
        lista.append(vetor[0])
        
    arquivo.close()
    print('Lista de frutas anexada')
#___________________________________________________________________________________
def limpar_lista():
    lista.clear()
    print('Você limpou a lista')
        
#___________________________________________________________________________________        
def menu():


    while True:
        print('\n\n------[ App Frutas ]------\n')
        print('1 = entrar fruta')
        print('2 = mostrar lista de frutas')
        print('3 = salvar lista de frutas')
        print('4 = recuperar lista de frutas')
        print('5 = anexar lista de frutas')
        print('6 = limpar lista de frutas')
        print('7 = sair do programa\n')
        
        opçao=int(input('Escolha a opção: '))
        if opçao == 1:
            entrar_fruta()
        elif opçao == 2:
            print(lista)
        elif opçao == 3:
            salvar_frutas()
        elif opçao == 4:
            recuperar_frutas()
        elif opçao == 5:
            anexar_frutas()
        elif opçao == 6:
            limpar_lista()
        elif opçao == 7:
            for x in range(200):
                print('Saindo...')#espera 1 segundo
                time.sleep(0.001)
            print('Fui!!')
            break
        else:
            print('Opção inválida!!')


menu()
