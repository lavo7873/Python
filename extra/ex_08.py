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
t.forward(20)
t.pendown()



t.pencolor('yellow')
t.fillcolor()
t.left(90)
t.forward(45)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(45)
t.end_fill()

t.penup()
t.right(90)
t.forward(20)
t.pendown()

t.pencolor('blue')
t.fillcolor()
t.left(90)
t.forward(70)
t.left(90)
t.forward(140)
t.left(90)
t.forward(140)
t.left(90)
t.forward(140)
t.left(90)
t.forward(70)
t.end_fill()

turtle.done()