import turtle
import math
  
  
# Function to draw rectangle
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
  
      
# Function to draw triangle    
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()
  
      
# Set the background color
screen = turtle.Screen ( )
screen.bgcolor("skyblue")
  
  
# Creating turtle object
tip = turtle.Turtle()
tip.color ("black")
tip.shape ("turtle")
tip.speed (2)
  
  
# Tree base
tip.penup()
tip.goto(100, -130)
tip.pendown()
drawRectangle(tip, 20, 40, "brown")
  
  
# Tree top
tip.penup()
tip.goto(65, -90)
tip.pendown()
drawTriangle(tip, 90, "lightgreen")
tip.penup()
tip.goto(70, -45)
tip.pendown()
drawTriangle(tip, 80, "lightgreen")
tip.penup()
tip.goto(75, -5)
tip.pendown()
drawTriangle(tip, 70, "lightgreen")

tip.penup()
tip.backward(800)
tip.pendown()

# the house
tip.fillcolor('cyan')
tip.begin_fill()
tip.right(90)
tip.forward(250)
tip.left(90)
tip.forward(400)
tip.left(90)
tip.forward(250)
tip.left(90)
tip.forward(400)
tip.right(90)
tip.end_fill()
  
# for top of
# the house
tip.fillcolor('brown')
tip.begin_fill()
tip.right(45)
tip.forward(200)
tip.right(90)
tip.forward(200)
tip.left(180)
tip.forward(200)
tip.right(135)
tip.forward(259)
tip.right(90)
tip.forward(142)
tip.end_fill()
  
# for door and
# windows
tip.right(90)
tip.forward(400)
tip.left(90)
tip.forward(50)
tip.left(90)
tip.forward(150)
tip.right(90)
tip.forward(200)
tip.right(180)
tip.forward(200)
tip.right(90)
tip.forward(200)
tip.right(90)
tip.forward(150)
tip.right(90)
tip.forward(200)
tip.right(90)
tip.forward(150)
tip.right(90)
tip.forward(100)
tip.right(90)
tip.forward(150)
tip.right(90)
tip.forward(100)
tip.right(90)
tip.forward(75)
tip.right(90)
tip.forward(200)
tip.right(180)
tip.forward(200)
tip.right(90)
tip.forward(75)
tip.left(90)
tip.forward(15)
tip.left(90)
tip.forward(200)
tip.right(90)
tip.forward(15)
tip.right(90)
tip.forward(75)

turtle.done()