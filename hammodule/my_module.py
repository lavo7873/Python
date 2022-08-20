def calculator(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    return sum, sub, mul


sum, sub, mul = calculator(10, 3)
print(sum, sub, mul)
