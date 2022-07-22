# Python program to find the largest
# number among the three numbers

def maximum(a, b, c):

	if (a >= b) and (a >= c):
		largest = a

	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
		
	return largest


# Driven code
a = float(input('Nhập số a :'))
b = float(input('Nhập số b :'))
c = float(input('Nhập số c :'))
print(maximum(a, b, c))
