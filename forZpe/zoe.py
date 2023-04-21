import turtle
from playsound import playsound

# Declaramos el espacio de ventana
turtle.screensize(400,300,"black")
turtle.speed(5) # La velocidad del cepillo se ajusta al máximo
turtle.color('#31A6DC','black') # Color
turtle.pensize(10) # Grosor
turtle.penup() # Levantamos la pluma

# Iniciamos dibujo Z
turtle.goto(-350, 200) 
turtle.pendown() # Bajamos la pluma
turtle.forward(200)
turtle.goto(-350,-50)
turtle.goto(-40,-50)
turtle.penup()

# Inicamos dibujo O
turtle.pendown()
#turtle.color('blue','black')
turtle.circle(130)

# Inciamnos dibujo E
turtle.penup()
turtle.circle(130,180)
turtle.left(180)
turtle.pendown()
turtle.forward(142)

turtle.left(-90)
turtle.forward(260)

turtle.left(-90)
turtle.forward(50)

turtle.left(180)
turtle.forward(200)
turtle.penup()
turtle.goto(100,210)
turtle.pendown()
turtle.forward(150)

turtle.goto(100,80)
turtle.left(180)
turtle.forward(40)
turtle.left(-180)
turtle.forward(140)

playsound("mananitas_recortado.mp3")

turtle.exitonclick()