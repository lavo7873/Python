# 1) hoa không xác định
for (var count = 0; count < 3; count++) {
  moveForward();
}
if (nectarRemaining() == 1) {
  getNectar();
}

# 8) lấy hoa
for (var count = 0; count < 4; count++) {
  moveForward();
}
if (nectarRemaining() == 1) {
  getNectar();
}
for (var count3 = 0; count3 < 3; count3++) {
  turnLeft();
  for (var count2 = 0; count2 < 3; count2++) {
      moveForward();
  }
  if (nectarRemaining() == 1) {
    getNectar();
  }
}