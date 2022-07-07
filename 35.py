import itertools
n = 10**6
numbers = [True]*n
primes = []
for i in range(2,n):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j] = False
circular_primes = []
def is_circular_prime(n):
    global numbers
    n = str(n)
    p = []
    for i in range(len(n)):
        n = n[1:]+n[0]
        p.append(n)
    for i in p:
        if not numbers[int(i)]:
            return False
    return True
for p in primes:
    if is_circular_prime(p):
        circular_primes.append(p)
print(len(circular_primes))
