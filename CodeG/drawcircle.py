import turtle

#đặt kích thước viền cho hình tròn là 5
turtle.pensize (5)

#đặt màu sắc cho viền hình tròn là màu đỏ
turtle.pencolor ("red")

#tuỳ chỉnh điểm bắt đầu vẽ hình tròn
turtle.Turtle().goto(-40, 120)
#đặt màu nền cho hình tròn là màu đỏ
turtle.fillcolor ("red")
turtle.begin_fill()

#đặt bán kính của hình tròn là 150
turtle.circle (150)
turtle.end_fill()
turtle.done()