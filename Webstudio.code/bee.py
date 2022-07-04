# 1) di chuyển nhặt hoa
for (var count = 0; count < 2; count++) {
  moveForward();
  moveForward();
  getNectar();
}

# 2) di chuyển tới nhặt hoa*4
moveForward();
moveForward();
for (var count = 0; count < 4; count++) {
  getNectar();
}

# 3) nhặt hoa và làm mật
moveForward();
for (var count = 0; count < 4; count++) {
  getNectar();
}
moveForward();
for (var count2 = 0; count2 < 4; count2++) {
  makeHoney();
}

# 4) đi thành hình chữ L nhặt hoa
for (var count = 0; count < 3; count++) {
  turnLeft();
  moveForward();
  getNectar();
  moveForward();
  getNectar();
}

# 6) di chuyển thành hình U cách 4 bước nhặt hoa rồi tiến bước làm mật
for (var count = 0; count < 3; count++) {
  turnLeft();
  moveForward();
  moveForward();
  moveForward();
  getNectar();
}
moveForward();
for (var count2 = 0; count2 < 3; count2++) {
  makeHoney();
}

# 7) đi chữ U ngang
for (var count = 0; count < 3; count++) {
  moveForward();
  moveForward();
  getNectar();
  turnRight();
}

#11) hình bật thang
for (var count = 0; count < 5; count++) {
  moveForward();
  turnRight();
  moveForward();
  getNectar();
  turnLeft();
}