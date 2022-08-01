while True:
    x = float(input("Nhập Giá Trị Của X :"))
    y = float(input("Nhập Giá Trị Của Y :"))
    if y > x:
        break
s = 0
i = x
while i <=y:
    s += i*i
    i += 1
print(f'Tổng Bình Phương Của {x} đến {y} là {s}')