#input turtle
import turtle

t = turtle

a = 90

#background color
t.bgcolor("lightblue")

t.speed(100)

#balance
t.penup()
t.backward(500)
t.right(a)
t.forward(300)
t.right(a)
t.forward(200)
t.right(a*2)
t.pendown()

#house
t.fillcolor('blue')
t.begin_fill()
t.forward(150)
t.left(a)
t.forward(200)
t.left(a)
t.forward(150)
t.left(a)
t.forward(200)
t.end_fill()

t.left(a)
t.forward(50)

#window
t.fillcolor('lightgreen')
t.begin_fill()
t.forward(50)
t.left(a)
t.forward(80)
t.left(a)
t.forward(50)
t.left(a)
t.forward(80)
t.end_fill()

t.left(a)
t.forward(100)

#sidehouse
t.fillcolor('yellow')
t.begin_fill()
t.left(30)
t.forward(100)
t.left(60)
t.forward(200)
t.left(120)
t.forward(100)
t.left(60)
t.forward(0)
t.end_fill()


#proof of house
t.fillcolor('hotpink')
t.begin_fill()
t.right(140)
t.forward(100)
t.left(92)
t.forward(115)
t.left(138)
t.forward(150)
t.end_fill()

#proofside of house
t.fillcolor('orange')
t.begin_fill()
t.left(30)
t.forward(100)
t.left(92)
t.forward(95)
t.left(87)
t.forward(114)
t.left(101)
t.forward(100)
t.end_fill()

#set up 1
t.penup()
t.left(5)
t.forward(40)
t.right(45)
t.pendown()

#windown
t.fillcolor('darkred')
t.begin_fill()
t.forward(60)
t.left(120)
t.forward(50)
t.left(60)
t.forward(60)
t.left(120)
t.forward(50)
t.end_fill()

#set up 2 next to tree
t.penup()
t.left(120)
t.forward(300)
t.right(85)
t.forward(50)
t.left(115)
t.pendown()

#tree bottom
t.fillcolor('brown')
t.begin_fill()
t.forward(40)
t.left(a)
t.forward(80)
t.left(a)
t.forward(40)
t.left(a)
t.forward(80)
t.end_fill()
t.right(a*2)
t.forward(80)

#tree top 1
t.fillcolor('lightgreen')
t.begin_fill()
t.left(a)
t.forward(60)
t.right(125)
t.forward(150)
t.right(110)
t.forward(150)
t.right(125)
t.forward(172)
t.right(125)
t.forward(150)
t.end_fill()

#tree top 2
t.fillcolor('lightgreen')
t.begin_fill()
t.left(125)
t.forward(75)
t.right(125)
t.forward(125)
t.right(110)
t.forward(125)
t.right(125)
t.forward(144)
t.end_fill()

t.penup()
t.right(125)
t.forward(125)
t.pendown()

#tree top 3
t.fillcolor('lightgreen')
t.begin_fill()
t.left(125)
t.forward(65)
t.right(125)
t.forward(115)
t.right(110)
t.forward(115)
t.right(125)
t.forward(132)
t.end_fill()

#set up for sun
t.penup()
t.right(a)
t.forward(200)
t.pendown()

#sun
t.fillcolor('yellow')
t.begin_fill()
t.circle(60)
t.end_fill()
t.right(a)
t.forward(80)
t.backward(80)

t.penup()
t.backward(120)
t.pendown()

t.backward(80)

t.penup()
t.forward(80)
t.pendown()

t.penup()
t.right(a)
t.forward(60)
t.left(a)
t.forward(60)
t.pendown()

t.right(a)
t.forward(80)

t.penup()
t.backward(200)
t.pendown()

t.backward(80)

t.penup()
t.forward(80)
t.right(a)
t.forward(50)
t.left(a)
t.forward(20)
t.left(a)
t.forward(10)
t.left(140)
t.forward(5)
t.pendown()

t.forward(60)

t.penup()
t.backward(179)
t.pendown()

t.backward(60)

t.penup()
t.forward(60)
t.right(40)
t.forward(70)
t.right(50)
t.forward(10)
t.pendown()

t.forward(60)

t.penup()
t.backward(179)
t.pendown()

t.backward(60)



#complete
turtle.done()
