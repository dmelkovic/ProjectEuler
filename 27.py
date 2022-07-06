n = 10**6
primes = [True]*n
for i in range(2,n):
    if primes[i]:
        for j in range(i*i,n,i):
            primes[j] = False
max_lenght = 0
coef_a = 0
coef_b = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 1
        lenght = 0
        while primes[n*n+a*n+b]:
            lenght += 1
            n += 1
        if lenght > max_lenght:
            coef_a, coef_b = a, b
            max_lenght = lenght

print(coef_a*coef_b)
    
