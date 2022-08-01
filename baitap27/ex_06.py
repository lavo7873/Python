# Convert integer 65 to ASCII Character ('A')
x = int(input("Nhập số : "))
y = chr(x)
print(type(y), y)
 
# Print A-Z
for i in range(65, 65+25):
    print(chr(i), end = " , ")
    
    
#===================================================
a = int(input("Nhập số : "))
b = ord(a)
print(type(b), b)
 

for i in range(65, 65+25):
    print(ord(i), end = " , ")