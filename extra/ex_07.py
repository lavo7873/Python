#importing turtle
import turtle
#function to draw square
def draw_square(t, size):
    #color for each side
    for c in ['red', 'green', 'blue','gray']:
        t.color(c)
        t.forward(size)
        t.left(90)
#setup the window       
turtle.setup(600,1000)

w = turtle.Screen()
#turtle object
te = turtle.Turtle()
#pensize
te.pensize(2)
#first sqaure size
p_size = 15
for i in range(25):
    #function call
    draw_square(te, p_size)
    #increasing size
    p_size = p_size +18      
    te.forward(16)        
    te.right(16)      
w.exitonclick()