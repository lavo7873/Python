#1) di chuyển với nhiều dòng code
moveForward();
moveForward();
moveForward();
moveForward();
moveForward();

#di chuyển nhiều lần với 2 dòng code
for (var count = 0; count < 5; count++) {
  moveForward();
}

#2) di chuyển tới 4 lần quẹo phải để đi xuống
for (var count = 0; count < 4; count++) {
  moveForward();
}
turnRight();
for (var count2 = 0; count2 < 5; count2++) {
  moveForward();
}

#3) di chuyển xuống 1 bước quẹo trái đi lên 5 bước
moveForward();
turnRight();
for (var count = 0; count < 5; count++) {
  moveForward();
}

#4) di chuyển thành hình chữ U
"""
quẹo phải đi xuống 2 dòng quẹo phải
đi tới 2 bước
quẹo phải đi tới 3 bước
"""
for (var count = 0; count < 5; count++) {
  turnRight();
  moveForward();
  moveForward();
}

/*
turnRight();
moveForward();
moveForward();
turnRight();
for (var count2 = 0; count2 < 2; count2++) {
  moveForward();
}
turnRight();
for (var count3 = 0; count3 < 3; count3++) {
  moveForward();
}
*/

""" 5)
đi xuống quẹo phải
đi xuống quẹo trái
x5 
"""
for (var count = 0; count < 5; count++) {
  moveForward();
  turnRight();
  moveForward();
  turnLeft();
}

# 6) quẹo hình chữ U
for (var count = 0; count < 3; count++) {
  moveForward();
}
turnRight();
for (var count2 = 0; count2 < 3; count2++) {
  moveForward();
}
turnRight();
for (var count3 = 0; count3 < 3; count3++) {
  moveForward();
}

# cách khác hình chữ U
for (var count2 = 0; count2 < 4; count2++) {
  moveForward();
  for (var count = 0; count < 2; count++) {
      moveForward();
  }
  turnRight();
}

/*
for (var count3 = 0; count3 < 3; count3++) {
  moveForward();
}
turnRight();
for (var count4 = 0; count4 < 3; count4++) {
  moveForward();
}
turnRight();
for (var count5 = 0; count5 < 3; count5++) {
  moveForward();
}
*/

# 7) di chuyển 
for (var count = 0; count < 5; count++) {
  moveForward();
}
turnLeft();
for (var count2 = 0; count2 < 5; count2++) {
  moveForward();
}
turnLeft();
for (var count3 = 0; count3 < 5; count3++) {
  moveForward();
}
turnLeft();
for (var count4 = 0; count4 < 3; count4++) {
  moveForward();
}
turnLeft();
for (var count5 = 0; count5 < 3; count5++) {
  moveForward();
}

""" 8)
di chuyển đi thẳng 2 xuống qua phải 2
"""
for (var count3 = 0; count3 < 2; count3++) {
  for (var count = 0; count < 2; count++) {
      moveForward();
  }
  turnLeft();
  for (var count2 = 0; count2 < 2; count2++) {
      moveForward();
  }
  turnRight();
}

# 9 ) di chuyển tới quẹo trái tiến 1 bước quẹo phải lặp lại 2 lần
for (var count2 = 0; count2 < 3; count2++) {
  for (var count = 0; count < 2; count++) {
      moveForward();
  }
  turnLeft();
  moveForward();
  turnRight();
}

#di chuyển thành chữ L
for (var count2 = 0; count2 < 3; count2++) {
  for (var count = 0; count < 2; count++) {
      moveForward();
  }
  turnLeft();
}