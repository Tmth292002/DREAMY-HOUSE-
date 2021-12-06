def HCN():
    w = 100
    h = 200
    import turtle
    a = turtle.Turtle()
    a.color("blue")
    a.pensize(10)
    a.pencolor("brown")
    a.begin_fill()

    for i in range(2):
        a.forward(w)
        a.right(90)
        a.forward(h)
        a.right(90)
    a.end_fill()
    turtle.exitonclick()


if __name__ == "__main__":
    HCN()


# def hcn():
#     import turtle
#     line = turtle.Turtle()

#     line.color("red", "yellow")
#     a = 300  # chieu dai hcn
#     b = 150  # chieu rong hcn

#     line.begin_fill()
#     for i in range(2):
#         line.forward(a)    # di lui``
#         line.left(90)
#         line.forward(b)     # di tien'
#         line.left(90)

#     line.penup()
#     line.forward(-200)     # lệnh nhảy
#     line.pendown()

#     for i in range(4):
#         line.forward(-b)  # di thang 100 pixel
#         line.right(90)  # quay phai 90 do

#     line.end_fill()
#     turtle.done()


# if __name__ == "__main__":
#     hcn()
