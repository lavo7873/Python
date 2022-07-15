import turtle

t = turtle

t.bgcolor("darkGreen")

for i in range (4):
    t.pencolor('red')
    t.fillcolor()
    t.forward(50)
    t.left(90)
    t.end_fill()


t.penup()
t.forward(25)
t.right(90)
t.forward(40)
t.pendown()



t.pencolor('yellow')
t.fillcolor()
t.left(90)
t.forward(60)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(60)
t.end_fill()

t.penup()
t.right(90)
t.forward(40)
t.pendown()

t.pencolor('blue')
t.fillcolor()
t.left(90)
t.forward(120)
t.left(90)
t.forward(200)
t.left(90)
t.forward(240)
t.left(90)
t.forward(200)
t.left(90)
t.forward(120)
t.end_fill()

turtle.done()