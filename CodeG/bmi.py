weight = float(input("Nhập Cân Nặng là bao nhiêu lbs : "))
height = float(input("Nhập chiều cao là bao nhiêu centimeter : "))

bmi = weight / height * height

if bmi >= 40:
    print("Béo phì cấp độ III")
elif 35 <= bmi < 40:
    print("Béo phì cấp độ II")
elif 30 <= bmi < 35:
    print("Béo phì cấp độ I")
elif 25 <= bmi < 30:
    print("Thừa cân")
elif 18.5 <= bmi < 25:
    print("Bình thường")
elif 17<= bmi < 18.5:
    print("Gầy cấp độ I")
elif 16 <= bmi < 17:
    print("Gầy cấp độ II")
elif bmi < 0:
    print("Erro, Mời nhập lại")
else:
    print("Gầy cấp độ III")