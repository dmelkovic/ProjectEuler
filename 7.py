n = 10**6
c = [True]*n
primes = []
for i in range(2,n):
    if c[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            c[j]=False
print(primes[10001-1])
    
