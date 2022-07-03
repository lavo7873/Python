import random
# nhập tên người dùng
name = input("Your Name:")

# chạy chương trình cho welcome
print(f"Welcome {name} to Guess Number!")

#chọn số
guess_number = 0

# chọn số từ 1 tới bao nhiêu tùy thích
com_guess = random.randint(1,50)

#hạn chế số lần
count = 0

#chương trình chạy
while guess_number != com_guess:
    guess_number = int(input("Please input your number 1-50: "))
    count += 1
    #số lần 5 lượt chơi
    if count > 5: 
        print("Please try again!")
        exit()
    if guess_number < com_guess:
        print("You are too low!")
    if guess_number > com_guess:
        print("You are too high!")
        
#kết quả
print("You Won,Amazing!!")
print(f"Computer guess is : {com_guess}")