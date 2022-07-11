#input turtle
import turtle

t = turtle

#background color
t.bgcolor("lightblue")

t.speed(100)

#balance
t.penup()
t.backward(500)
t.right(90)
t.forward(300)
t.right(90)
t.forward(200)
t.right(180)
t.pendown()

#house
t.fillcolor('blue')
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.left(90)
t.forward(200)
t.end_fill()

t.left(90)
t.forward(50)

#window
t.fillcolor('lightgreen')
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.end_fill()

t.left(90)
t.forward(100)

#sidehouse
t.left(30)
t.forward(150)
t.left(60)
t.forward(150)
t.left(120)
t.forward(150)
t.left(60)
t.forward(150)




#complete
turtle.done()
