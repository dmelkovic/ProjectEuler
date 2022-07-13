"""
we want to minimize n/phi(n). That means we want to maximize phi(n)
phi(n) is n-1 if n is prime, but then phi(n) wont be permutation of n.
Assume that n consist of 2 primes. 
"""
def is_perm(a,b):
    a = str(a)
    b = str(b)
    ap = [0]*10
    bp = [0]*10
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            ap[int(a[i])] += 1
            bp[int(b[i])] += 1
        if ap == bp:
            return True
        return False

n = 10**7
n1 = 10**6
n2 = int(n**.5)
numbers = [True]*n1
primes = []
for i in range(2,n1):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n1,i):
            numbers[j] = False

minimum = 10**7
minimum_n = 0
divisor = 0
while primes[divisor] < n2: divisor += 1
#separete primes<sqrt(n) bacause smallest divisor is in that range
for i in range(divisor,-1,-1):
    for j in range(0,len(primes)):
        if primes[i]*primes[j]>n:
            break
        if primes[i]*primes[j]/(primes[i]-1)/(primes[j]-1) < minimum:
            if is_perm(primes[i]*primes[j], (primes[i]-1)*(primes[j]-1)):
                minimum = primes[i]*primes[j]/(primes[i]-1)/(primes[j]-1)
                minimum_n = primes[i]*primes[j]
print(minimum_n)

