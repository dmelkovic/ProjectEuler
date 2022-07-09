n = 10**6
numbers = [True]*n
primes = []
for i in range(2,n):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j] = False
#lets precompute sum of first k  primes.
sums = []
s = 0
for p in primes:
    s += p
    sums.append(s)
max_len = 0
prime = 0
for i in range(0,len(sums)):
    for j in range(i+1,len(sums)):
        if sums[j]-sums[i]<n:
            if numbers[sums[j]-sums[i]]:
                if j-i > max_len:
                    max_len = j - i
                    prime = sums[j]-sums[i]
        else:
            break
print(prime)
