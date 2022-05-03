#funcional.py
#Uso de map em listas

#Tipos de programação (paradigmas)
#Imperativo
#Orientado à objetos ou eventos
#Funcional

#Objetivo: converter uma lista de strings em inteiros
lista=['1','3','5','7']
print(lista)

#1. Usando o loop for (paradigma imperativo)
novaLista=[]
for x in lista: novaLista.append(int(x))
print('Ciclo for:', novaLista)

#2. Usando "list comprehension" (compreensão de listas) - paradigma imperativo
novaLista=[int(x) for x in lista]
print ('List comprehension:', novaLista)

#3. Usando map com função nomeada - paradigma funcional
def converter(x): return int(x)

print(list(map(converter, lista)))

#4. Usando map com função anônima - paradigma funcional
print(list(map(lambda x: int(x), lista)))
