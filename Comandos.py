#Comandos
#https://www.w3schools.com/python/python_ref_string.asp
#__________________________________________________________________________________________________________
#capitalize()
#O primeiro caractere é convertido em maiúsculas e os demais são convertidos em minúsculas:
txt = "python eh daora!)"

x = txt.capitalize()

print (x)
#__________________________________________________________________________________________________________
#casefold()
#deixa os caracteres em minusculo
txt = "OI EU ADORO ABACAXIS!"#-> oi eu adoro abacaxis!

x = txt.casefold()

print(x)
#__________________________________________________________________________________________________________
#center()
#Deixa a palavra/frase centralizada
txt = "banana"

x = txt.center(50)#-> distância das bordas

print(x)
#__________________________________________________________________________________________________________
#count()
#conta quantas letras/palavras especificas tem na frase
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple") #2

print(x)
#__________________________________________________________________________________________________________
#encode()
#mostra a versão codificada da string
txt = "My name is Ståle"

x = txt.encode()#b'My name is St\xc3\xe5le'

print(x)
#__________________________________________________________________________________________________________
#endswith()
#Retorna verdadeiro se a string termina com um valor especifico
txt = "Hello, welcome to my world."

x = txt.endswith(".")#True

print(x)
#__________________________________________________________________________________________________________
#expandtabs()
#configura o tamanho do tab da string
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2) #H e l l o

print(x)
#__________________________________________________________________________________________________________
#find()
#Pesquisa a string por um valor especificado e retorna a posição de onde foi encontrado
txt = "Hello, welcome to my world."

x = txt.find("welcome")#7

print(x)
#__________________________________________________________________________________________________________
#format()
#Altera determinados valores em um string
txt = "For only {price:.2f} dollars!" #49.00
print(txt.format(price = 49))
#__________________________________________________________________________________________________________
#index()
#Mostra quantos caracteres tem em uma string especifica
txt = "Hello, welcome to my world."

x = txt.index("welcome")#7

print(x)
#__________________________________________________________________________________________________________
#isalnum()
#Retorna verdadeiro se a string possuir números
txt = "Company12"

x = txt.isalnum()#True

print(x)
#__________________________________________________________________________________________________________
#isalpha()
#Retorna verdadeiro se a string possuir APENAS letras
txt = "CompanyX"

x = txt.isalpha()#True

print(x)
#__________________________________________________________________________________________________________
