num = float(input("Nhập số tiền bạn thanh toán : "))
if num >= 150:
    print("Bạn được discount 50$ số tiền là", num - 50)
elif num >=100:
    print("Bạn được discount 25$ số tiền là", num - 25)
elif num >=75:
    print("Bạn được discount 15$ số tiền là", num - 15)
elif num <0:
    print("Bạn cần thanh toán lại tiệm số tiền là :", num)
else:
    print("Bạn không được discount số tiền là", num)