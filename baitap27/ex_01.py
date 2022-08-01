n = int(input("Nhập số cần tính giai thừa: "))
 
i = 1
m = 1

while i<=n:
    m = m*i
    i += 1

print(f'Giai thừa là {n} bằng {m}')
