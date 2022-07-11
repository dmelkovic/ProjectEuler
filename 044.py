pentagonals = set(x*(3*x-1)/2 for x in range(1,2500))
for a in pentagonals:
  for b in pentagonals:
    if a-b in pentagonals and a+b in pentagonals:
       print(int(a-b))
