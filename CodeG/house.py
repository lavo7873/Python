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
t.left(90)
t.forward(80)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.end_fill()
t.right(180)
t.forward(80)

#tree top 1
t.fillcolor('lightgreen')
t.begin_fill()
t.left(90)
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
t.right(90)
t.forward(300)

#sun

# set parameters
Width = 700
Height =700
T = "SUN"
# open window
t.open_window(Width, Height, Title)
  
# Set the background color
t.set_background_color(t.csscolor.BLUE)
  
# Get ready to draw
t.start_render()
  
# Draw a sun
t.draw_circle_filled(500, 550, 40, t.color.YELLOW)
  
# Rays to the left, right, up, and down
t.draw_line(500, 550, 400, 550, t.color.YELLOW, 3)
t.draw_line(500, 550, 600, 550, t.color.YELLOW, 3)
t.draw_line(500, 550, 500, 450, t.color.YELLOW, 3)
t.draw_line(500, 550, 500, 650, t.color.YELLOW, 3)
  
# Diagona
t.draw_line(500, 550, 550, 600, t.color.YELLOW, 3)
t.draw_line(500, 550, 550, 500, t.color.YELLOW, 3)
t.draw_line(500, 550, 450, 600, t.color.YELLOW, 3)
t.draw_line(500, 550, 450, 500, t.color.YELLOW, 3)
  
# Finish drawing
t.finish_render()







#complete
turtle.done()
