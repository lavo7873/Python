# 1) di chuyển thành hình vuông
for (var count = 0; count < 1; count++) {
  moveForward(100);
  turnRight(90);
  moveForward(100);
  turnRight(90);
  moveForward(100);
  turnRight(90);
  moveForward(100);
}
# 2) di chuyển thành hình vuông cách 2:
for (var count = 0; count < 4; count++) {
  moveForward(100);
  turnRight(90);
}

# 3) vẽ 8 cây thành giống hình ngôi sao
for (var count = 0; count < 8; count++) {
  penColour(colour_random());
  moveForward(100);
  moveBackward(100);
  turnRight(45);
}

# 4) tô màu ra hình tròn
for (var count = 0; count < 1000; count++) {
  penColour(colour_random());
  moveForward(100);
  moveBackward(100);
  turnRight(1);
}

#5) vẽ thành hình bát giác
for (var count = 0; count < 8; count++) {
  moveForward(100);
  turnRight(45);
}

#6) vẽ hình tròn
for (var count = 0; count < 400; count++) {
  moveForward(1);
  turnRight(1);
}

# 7)vẽ thành hình chữ V

turnRight(45);
moveForward(50);
turnLeft(90);
moveForward(50);

# 8) vẽ thành hình ngôi sao 8 cạnh mà viền bên ngoài
for (var count = 0; count < 8; count++) {
  penColour(colour_random());
  turnRight(45);
  moveForward(50);
  turnLeft(90);
  moveForward(50);
}

""" 9) vẽ hình ngôi sao 5 cánh ở viền ngoài
nhiều hình tròng vào nhau. chỉ cần di chuyển góc xuống 30 degree
"""
for (var count = 0; count < 24; count++) {
  penColour(colour_random());
  turnRight(45);
  moveForward(50);
  turnLeft(90);
  moveForward(50);
  turnLeft(30);
}

# 10 ) di chuyển thành hình vuông méo 
turnLeft(60);
moveForward(100);
turnRight(120);
moveForward(100);
turnRight(60);
moveForward(100);
turnRight(120);
moveForward(100);

# 11) di chuyển hình vuông 3 D
for (var count = 0; count < 3; count++) {
  penColour(colour_random());
  turnLeft(60);
  moveForward(100);
  turnRight(120);
  moveForward(100);
  turnRight(60);
  moveForward(100);
  turnRight(120);
  moveForward(100);
}

# 12) di chuyển thành hình vuông 3D tròng vào nhau;
for (var count = 0; count < 9; count++) {
  penColour(colour_random());
  turnLeft(60);
  moveForward(100);
  turnRight(120);
  moveForward(100);
  turnRight(60);
  moveForward(100);
  turnRight(120);
  moveForward(100);
  turnRight(90);
}