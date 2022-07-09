n = 10000
numbers = [True]*n
primes = []
for i in range(2,n):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j] = False
for i in range(3,n,2):
    if not numbers[i]:  # we already know composite numbers
        p = 0
        while primes[p] < i:
            x = ((i - primes[p])/2)**.5
            if x == int(x):
                break
            else:
                p += 1
        if primes[p]>i: #we fail if we get trough all primes less than i
            print(i)
            break
