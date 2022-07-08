#import thư viện
import turtle

#khởi tạo đối tượng
t = turtle

#vẽ
t.delay(20)
t.pencolor('red')
t.pensize(10)
t.fillcolor('gray')
t.begin_fill()
t.forward(100)
t.right(90)
t.pencolor('blue')
t.forward(100)
t.right(90)
t.pencolor('green')
t.forward(100)
t.right(90)
t.pencolor('yellow')
t.forward(100)
t.right(90)

t.pencolor('lightblue')
t.left(50)
t.forward(90)

t.pencolor('pink')
t.right(105)
t.forward(78)

t.end_fill()


#kết thúc vẽ
turtle.done()