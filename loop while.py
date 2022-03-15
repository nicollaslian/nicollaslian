
#loop_while.py

print ('Exemplo loop while')

senha = 0
tentativas = 0;
total_tentativas = 5

while senha != 123:
    senha = int(input('Digite a senha:'))
    tentativas+= 1

    if(senha == 123):
        print('Bem vindo ao sistema')
    else:
        if(tentativas>=total_tentativas):
            print('Senha Bloqueada!')
            break
        else:
            print('Restam {} tentativas'.format(total_tentativas-tentativas))
