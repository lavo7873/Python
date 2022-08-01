while True:
    n = int(input("Nhập số nguyên n: "))
    if n > 0:
        break
s = 0 
i = 1
while i < n:
    if n%i == 0:
        s = s + i
    i += 1
if s == n:
    print(f"{n} là số hoàn chỉnh")
else:
    print(f"{n} không phải là số hoàn chỉnh")
    