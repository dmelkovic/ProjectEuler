"""
n/d < 3/7, that means 7n<3d
we will go trough d<=10**6. That means we know d and we want to find highest n
possible. n < 3d/7. That is highest n to be as close to 3/7.
Now we want to be as closest to the left as possible.
That means 3/7-n/d should be minimal. (3d-7n)/7d should be minimal and
since 7d > 0 we want minimum of 3d-7d.
Oh and n,d are coprimes :)
"""
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
best_d = 10**6
best_n = 1
numerator = 0
for d in range(2,10**6+1):
    n = int((3*d-1)/7)
    if n/d > best_n/best_d:
        best_n = n
        best_d = d
print(best_n//gcd(best_n,best_d))
