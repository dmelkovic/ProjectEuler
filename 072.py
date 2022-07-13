"""
fraction n/d is reduces if gcd(n,d)=1
We want know number of reduced fraction for given d.
How many numbers are coprime to d which are less than d??
Euler totient function is exactly what will tell us.
"""
m = 10**6+1
phi = [x for x in range(m)]
for i in range(2,m):
    if phi[i] == i:
        for j in range(i,m,i):
            phi[j] = phi[j]*(i-1)//i
print(sum(phi[2:]))
