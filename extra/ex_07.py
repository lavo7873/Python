import turtle

colors = ['blue','red','green',]

t = turtle.Pen()


for x in range(360):
   t.pencolor(colors[x%2])
   t.width(x//100 + 1)
   t.forward(x)
   t.left(90)

turtle.done()