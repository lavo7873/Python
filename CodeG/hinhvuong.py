import turtle

a = int(input("Nhập độ dài của hình vuông : "))

t = turtle.Turtle()
t.hideturtle()
t.pencolor("red")
edge = 0

while edge < 4:
    t.forward(a)
    t.right(90)
    edge += 1

turtle.done()