"""
Straightforward approach. Check gcd of every n/d which satisfy 1/3<n/d<1/2.
It's bit slow.
"""
def gcd(a,b):
    while a!=0:
        if a>b:
            a=a%b
        else:
            a,b=b,a
    return b
result = 0
for d in range(2,12000+1):
    for n in range(d//3,d//2):
        if gcd(n,d) == 1:
            result += 1
print(result)
