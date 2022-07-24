import math
import turtle

r = int(input("Enter The Radius : "))

t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color("red")
t.circle(r)
turtle.done()

c = 2 * math.pi * r
s = math.pi *r*r

print("Chu Vi Của hình tròn có bán kính = {r} là {c}".format(r=r, c=c))
print("Diện Tích của hình tròn có bán kính = {r} là {s}".format(s=s, r=r))

