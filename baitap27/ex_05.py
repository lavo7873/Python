n = int(input("Nhap so: "))
tong = 0
for i in range(1, n+1):
    tong = tong + 1/i
print(f"{tong: .5f}")