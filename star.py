import turtle

star = turtle.Turtle()
star.penup()
star.goto(-210, -150)
star.pendown()
star.fillcolor("red")
star.pensize(3)
star.pencolor("blue")
# star.speed(1)
star.begin_fill()

for i in range(5):
    star.forward(100)
    star.right(144)
star.end_fill()
turtle.done()
