#if_else.py
#elif = else if
#int converte string em inteiro:'30' => 30
temp=int(input('Entre com a temperatura:'))

if temp < 0:
    print('Congelando...')
    
elif 0 <= temp <= 20:
    print('Frio')

elif 21 <= temp <= 25:
    print('Normal')

elif 26 <= temp <= 35:
    print('Quente')

else:
    print('Muito Quente!')
