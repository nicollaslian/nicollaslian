import turtle
turtle.bgcolor('black')
p=turtle.Pen()

#        0       1      2      3        4        5      6       7     8        9
cores=["red","yellow","blue","green","orange","pink","white","cyan","brown","purple"]

#           0         1        2        3        4        5       6       7        8         9
animais=['cachorro','gato','elefante','peixe','camelo','ovelha','tigre','lobo','tartaruga','leão']

for x in range(200): #0,1,2,3,4,5,6,7...99

    p.penup()
    p.forward(x*3)
    resto=x%len(animais) #retorna sempre um valor de 0 a 9
    p.pencolor(cores[resto])
    animal=animais[resto] #0 a 9
    p.write(animal,font=('Arial',int (x*0.6),'bold'))
    p.left(360/(len(animais)+2))
    
    
