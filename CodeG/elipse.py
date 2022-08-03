# Import turtle
import turtle

# Function used to draw the ellipse
def drawEllipse(rad):
    
    # Loop for to dra two arcs of ellipse
    for i in range(2):
        
        # Draw arc
        turtle.circle(rad, 90)
        turtle.circle(rad//2, 90)

# Set the turtle secreen
scr = turtle.Screen()

# Set screen size
scr.setup(600, 600)
 
# Set screen color
scr.bgcolor('black')
 
# Create a list to store the color of ellipse
color = ['violet','blue','green','yellow', 'orange','red']
 
# Used to store the ellipse orientation agle
angle = 10

# Used to store color list index 
color_index = 0
 
# Set the spped of turtle
turtle.speed(100)

# Used for loop counter
i = 1
 
# loop for draw the ellipses
while i <= 36:
     
    # Set the ellipse orientation at negative angle 
    turtle.seth(-angle)
     
    # Set the color of the turlte
    turtle.color(color[color_index])  
    
    # Call method to draw the ellipse of radius 100
    drawEllipse(120)
     
    # Increase the ellipse orientation agle by 10
    angle += 10
    
    # If index of color is 5
    if color_index == 5:
        
        # Set it to 0
        color_index = 0
        
    # If index of color is less than 5
    else:
        
        # Increase color index by 1
        color_index += 1
    
    # Increase the loopcounter by 1
    i += 1
    
# Hide the turtle
turtle.hideturtle()

turtle.done()