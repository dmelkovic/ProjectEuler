#its easy to find triangle number equal to hexagonal.
# lets have hexagonal number with index m
# we can check if triangular number with index 2m-1 is equal to hexagonal
# T_(2m-1) = (2m-1)(2m-1+1)/2 = (2m-1)(2m)/2 = m(2m-1) = H_m
# we just need to check if pentagonal is equal to hexagonal number
# n(3n-1)=2H
# 3n^2-n-2H = 0
# n = (1+(1+24h)^.5)/6
for n in range(144,100000):
    h = n*(2*n-1)
    p = (1+(1+24*h)**.5)/6
    if p == int(p):
        print(h)
        break
