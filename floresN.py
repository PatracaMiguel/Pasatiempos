import turtle

def dibujar_flor():
    turtle.color('yellow')
    turtle.begin_fill()
    for _ in range(36):
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()

def dibujar_tallo():
    turtle.color('green')
    turtle.right(90)
    turtle.forward(300)
    turtle.right(270)

turtle.speed(0)
turtle.bgcolor('black')

turtle.penup()
turtle.goto(-100, -50)  
turtle.pendown()

dibujar_flor()
turtle.penup()
turtle.goto(0, -100)  
turtle.pendown()

dibujar_tallo()
turtle.hideturtle()
turtle.done()

