# Name : Lam Vinh Vong
# Class : Cmpe_120

#exercise 1 :


letter1 = str(input("Input the letter you want to change :"))
def uppercase(letter1):
    return letter1.upper()
print(uppercase(letter1))


#exercise 2 :
letter2 = str(input("Input the letter you want to change :"))
def lowercase(letter2):
    return letter2.lower()
print(lowercase(letter2))


#exercise 3:
letter3 = str(input("Input the letter you want to change :"))
def is_alphabet(letter3):
    return letter3.isalpha()
print(is_alphabet(letter3))

#exercise 4:
l_str = input("Enter any value: ")
any word and a b c d _
if l_str.isdigit():
    print("This is integral")
else:
    print("This is string ")

#exercise 5:
n = str(input("Input any value : "))
n.split()
c=0
s='[@_!#$%^&*()<>?/\|}{~:]'
for i in range(len(n)):
    if n[i] in s:
      c+=1   
if c:
    print("string is not accepted")
else:
    print("string accepted")