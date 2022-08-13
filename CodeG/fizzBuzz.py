m = int(input("Nhập số bất kì cho m : "))
n = int(input("Nhập số bất kì cho n : "))

if m > n:
      print("Số kết thúc cần lớn hơn số bắt đầu!")
else:
      for i in range(m, n + 1):
            if i%3 == 0 and i % 5 == 0:
                  print("FizzBuzz")
            elif i % 5 == 0:
                  print("Buzz")
            elif i % 3 == 0:
                  print("Fizz")
            else:
                  print(i)