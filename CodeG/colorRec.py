import turtle

color = input("Nhập màu hoặc mã màu: ")
w = float(input("Nhập chiều dài hình chữ nhật :"))
h = float(input("Nhập chiều cao hình chữ nhật : "))

t = turtle.Turtle()
t.hideturtle()

t.color(color)
t.begin_fill()

t.forward(w)
t.right(90)

t.forward(h)
t.right(90)

t.forward(w)
t.right(90)

t.forward(h)
t.end_fill()

turtle.done()

c = 2*(w + h)
s = w*h

print("Chu Vi hình chữ nhật (dài = {w}, rộng = {h} là {c}".format(w=w, h=h, c=c))
print("Diện tích của hình chữ nhật (dài = {w}, rộng = {h}) là {s}".format(w=w, h=h, s=s))
