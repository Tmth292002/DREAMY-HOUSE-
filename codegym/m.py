
def ngoinha():
    import turtle
    turtle.bgcolor("aqua")
    hcn = turtle.Turtle()
    hcn.speed(5)
    # ve mat truoc cua nha
    hcn.pensize(2)
    hcn.penup()
    hcn.goto(-300, -100)
    hcn.pendown()
    hcn.fillcolor("Blue")
    hcn.begin_fill()
    a = 150
    b = 200
    a1 = a-50
    for i in range(2):
        hcn.fd(a)
        hcn.rt(90)
        hcn.fd(b)
        hcn.rt(90)
    hcn.end_fill()

    # ve mai nha trước
    hcn.fillcolor("fuchsia")
    hcn.begin_fill()
    hcn.lt(60)
    hcn.fd(150)
    hcn.rt(120)
    hcn.fd(150)
    hcn.end_fill()

    # vẽ mái nhà phía sau
    hcn.fillcolor("orange")
    hcn.begin_fill()
    for i in range(4):
        hcn.lt(90)
        hcn.fd(a)
    hcn.end_fill()

    # vẽ mặt bên ngoi nhà
    hcn.fillcolor("yellow")
    hcn.begin_fill()
    hcn.rt(30)
    hcn.fd(200)
    hcn.lt(120)
    hcn.fd(150)
    hcn.lt(60)
    hcn.fd(200)
    hcn.end_fill()

    # vẽ cửa sổ của ngôi nhà
    hcn.lt(120)
    hcn.fd(a1)
    hcn.lt(60)
    hcn.penup()
    hcn.fd(50)
    hcn.pendown()
    hcn.fillcolor("red")
    hcn.begin_fill()
    for i in range(2):
        hcn.fd(50)
        hcn.lt(120)
        hcn.fd(50)
        hcn.lt(60)
    hcn.end_fill()

    # ve cua chinh cua ngoi nha
    hcn.penup()
    hcn.goto(-260, -300)
    hcn.pendown()
    hcn.lt(180)
    hcn.fillcolor("green")
    hcn.begin_fill()
    for i in range(2):
        hcn.fd(100)
        hcn.rt(90)
        hcn.fd(70)
        hcn.rt(90)
    hcn.end_fill()


def cay():
    import turtle
    import math
    a = 40
    b = 100
    a1 = 20
    b1 = math.sqrt(2)*b/2
    c = turtle.Turtle()
    c.speed(5)
    c.penup()
    c.goto(100, -180)
    c.pendown()
    # vẽ thân cây
    c.fillcolor("red")
    c.begin_fill()
    for i in range(2):
        c.fd(a)
        c.rt(90)
        c.fd(b)
        c.rt(90)
    c.end_fill()
    c.fd(a1)
    # c.fd(a1)
    # c.rt(90)
    # c.fd(b)
    # c.rt(90)
    # c.fd(a)
    # c.rt(90)
    # c.fd(b)
    # c.rt(90)
    # c.fd(a1)
    # c.end_fill()

    # vẽ các tầng lá thông
    c.fillcolor('chartreuse')
    c.begin_fill()
    for i in range(3):
        c.fd(b1)
        c.lt(135)
        c.fd(b)
        c.rt(135)
    c.rt(135)
    for i in range(3):
        c.fd(b)
        c.lt(135)
        c.fd(b1)
        c.rt(135)
    c.end_fill()
    # turtle.done()


def sun():
    import turtle
    s = turtle.Turtle()
    turtle.bgcolor("aqua")
    a = 40
    b = 200
    c = 100
    s.speed(3)
    # vẽ các đường tia mat tro
    s.penup()
    s.goto(a-c, b)
    s.pendown()
    s.goto(a+c, b)
    s.penup()
    s.goto(a, b-c)
    s.pendown()
    s.goto(a, b+c)
    s.penup()
    s.goto((2*a-c)/2, (2*b+c)/2)
    s.pendown()
    s.goto((2*a+c)/2, (2*b-c)/2)
    s.penup()
    s.goto((2*a-c)/2, (2*b-c)/2)
    s.pendown()
    s.goto((2*a+c)/2, (2*b+c)/2)

    # vẽ mặt trời
    s.penup()
    s.goto(a, (2*b-c)/2)
    s.pendown()
    s.fillcolor("yellow")
    s.begin_fill()
    s.circle(c/2)
    s.end_fill()
    turtle.done()


def main():
    ngoinha()
    cay()
    sun()


if __name__ == "__main__":
    main()
