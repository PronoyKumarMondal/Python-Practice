x = y = 0
sum = 0
while (x < 10):
  y = x - 3
  while (y < 3):
    sum = x - y * 2
    print(sum)
    y = y + 1
  if (x > 7):
    x += 1
  else:
    x += 3
sum = x - y * 2
print(sum)