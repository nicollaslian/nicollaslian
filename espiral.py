#espiral1.py

import turtle
p=turtle.Pen()
p.speed(100)

turtle.bgcolor("black")
#        0      1       2       3       4        5
cores=["red","yellow","blue","green","orange","purple"]

lados=int(turtle.numinput("Escolha entre 2 e 6","Número de lados"))



for x in range(1000):
    resto=x%4 #devolve 0,1,2 ou 3
    cor=cores[resto]
    p.pencolor(cor)
    p.forward(x*0.2)
    p.left(360/(lados+1))

