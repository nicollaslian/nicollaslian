Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> texto='bom dia'
>>> texto.capitalize()
'Bom dia'
>>> texto.title()
'Bom Dia'
>>> texto='BOM DIA'
>>> texto.lower()
'bom dia'
>>> texto.casefold()
'bom dia'
>>> texto='bom dia'
>>> texto.upper()
'BOM DIA'
>>> frase='o rato roeu a roupa do rei de Roma'
>>> frase.count('r')
4
>>> frase.count('R')
1
>>> inicial=frase.find('roupa')
>>> tamanho=len('roupa)
	    
SyntaxError: EOL while scanning string literal
>>> tamanho=len('roupa)
	    
SyntaxError: EOL while scanning string literal
>>> tamanho=len('roupa')
>>> final=inicial+tamanho
>>> palavra=frase[inicial:final]
>>> '0123456789'.isalnum()
True
>>> 'abcdefghij'.isalnum()
True
>>> '0123456ABC'.isalnum
<built-in method isalnum of str object at 0x000001DCCB501AF0>
>>> '0123456ABC'.isalnum()
True
>>> '01234567 9'.isalnum()
False
>>> ',$1%&*()11'.isalnum()
False
>>> 'abcdefg'.isalpha()
True
>>> 'abcd123'.isalpha()
False
>>> '0123456789'.isnumeric()
True
>>> 'abcdefghij'.isnumeric()
False
>>> 'abcdef0123'.isnumeric()
False
>>> texto='             abc       def        '
>>> saudaçao.starswith('bom')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    saudaçao.starswith('bom')
NameError: name 'saudaçao' is not defined
>>> saudaçao='bom dia'
>>> saudaçao=startswith('bom')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    saudaçao=startswith('bom')
NameError: name 'startswith' is not defined
>>> saudaçao.startswith('bom')
True
>>> saudaçao.startswith('BOM')
False
>>> saudaçao.endswith('dia')
True
>>> saudaçao.endswith('DIA')
False
>>> frase.split(' ')
['o', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma']
>>> frase.split('r')
['o ', 'ato ', 'oeu a ', 'oupa do ', 'ei de Roma']
>>> expressao='123+456+789'
>>> lista=expressao.split('+')
>>> lista
['123', '456', '789']
>>> final
19
>>> palavra
'roupa'
>>> frase
'o rato roeu a roupa do rei de Roma'
>>> soma=0
>>> for valor in lista:
	soma+= int(valor)
	print(soma)

	
123
579
1368
>>> frase.replace('r','1')
'o 1ato 1oeu a 1oupa do 1ei de Roma'
>>> texto='você é uma má pessoa'
>>> texto.replace('má','ótima')
'você é uma ótima pessoa'
>>> saudaçao='Bem vindo Nicollas ao python'
>>> nome=input('Digite seu nome: ').lower().title()
Digite seu nome: Nicollas
>>> print(saudaçao.replace('Nicollas',nome))
Bem vindo Nicollas ao python
>>> texto2='esse é u8m texto\nconsiderando que foi digitado\nem um editor de texto simples'
>>> for linha in texto.splitlines():
	print(linha)

	
você é uma má pessoa
>>> preço=1.99
>>> nome='Nicollas Lian'
>>> idade=14
>>> print('Compre apenas por R$%.2f'%preço)
Compre apenas por R$1.99
>>> print('Meu nome é %s e tenho %d anos'%(idade,nome))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print('Meu nome é %s e tenho %d anos'%(idade,nome))
TypeError: %d format: a number is required, not str
>>> print('Meu nome é %s e tenho %d anos'%('idade','nome'))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print('Meu nome é %s e tenho %d anos'%('idade','nome'))
TypeError: %d format: a number is required, not str
>>> print('Compre por apenas R${:.2f}'.format(preço))
Compre por apenas R$1.99
>>> print('Meu nome é {} e tenho {} anos'.format(nome,idade))
Meu nome é Nicollas Lian e tenho 14 anos
>>> print(f'Compre por apenas R$ {preço:.2f}')
Compre por apenas R$ 1.99
>>> import math
>>> print(f'O valor de pi é aproximadamente {math.pi:.3f}')
O valor de pi é aproximadamente 3.142
>>> print(F'Meu nome é {nome} e tenho {idade} anos')
Meu nome é Nicollas Lian e tenho 14 anos
>>> print('Meu nome é %s e tenho %d anos'%{idade,nome})
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print('Meu nome é %s e tenho %d anos'%{idade,nome})
TypeError: not enough arguments for format string
>>> print('Meu nome é %s e tenho %d anos'%(idade,nome))
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print('Meu nome é %s e tenho %d anos'%(idade,nome))
TypeError: %d format: a number is required, not str
>>> print('Meu nome é %s e tenho %d anos'%(nome,idade))
Meu nome é Nicollas Lian e tenho 14 anos
>>> 