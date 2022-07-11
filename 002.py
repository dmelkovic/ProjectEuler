a = 1
b = 1
s = 0
while b < 4*10**6:
    a,b = b, a+b
    if b%2==0:
        s+=b
print(s)
