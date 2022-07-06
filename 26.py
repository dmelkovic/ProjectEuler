# useful article https://mathworld.wolfram.com/FullReptendPrime.html

n = 1000
c = [True]*n
primes = []
for i in range(2,n):
    if c[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            c[j] = False
longest = 0
number = 0
for p in primes:
    for i in range(1,p):
        if pow(10,i,p)==1:
            if i > longest:
                number = p
                longest = i
            break #smallest i that 10^i is congruent to 1 mod p
print(number)
