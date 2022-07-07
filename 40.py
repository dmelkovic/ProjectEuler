d = " "
x = 0
while len(d) < 1000001:
  x += 1
  d += str(x)

print (int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) *
  int(d[10000]) * int(d[100000]) * int(d[1000000]))
