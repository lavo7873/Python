n = int(input("nhập số n: "))
i = 1
j = n - 1
while i <= n:
    step = " " * j
    s1 = "*" * i
    s2 = "*" * (i-1)
    print(step + s1 + s2)
    i += 1
    j -= 1
z = 1
n = n -1
while n >= 1:
    step2 = " " * z
    s3 = "*" * n
    s4 = "*" * (n-1)
    print(step2 + s3 + s4)
    n -=1
    z += 1 