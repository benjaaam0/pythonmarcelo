import turtle

# Configuración inicial
wn = turtle.Screen()
wn.bgcolor("lightpink")  # Cambiamos el color de fondo
red = turtle.Turtle()

# Función para dibujar la curva más grande
def curve():
    for i in range(200):
        red.right(1)
        red.forward(2)  # Aumentamos la distancia para hacer el corazón más grande

# Función principal para dibujar el corazón con mensaje
def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(224)  # Longitud aumentada para hacer el corazón más grande
    curve()
    red.left(120)
    curve()
    red.forward(224)
    red.end_fill()

    # Escribir "Un te quiero" en el corazón
    red.up()
    red.setpos(-70, -20)  # Posiciona el cursor para el texto dentro del corazón
    red.down()
    red.color('white')
    red.write("te quiero jireh aunque seas mensita", align="center", font=("Arial", 18, "bold"))

# Dibujar el corazón y el mensaje
red.speed(2)  # Ajustamos la velocidad de dibujo
heart()

# Finalizar el programa
red.hideturtle()
turtle.done()




















