"""I started solving this problem hard way – for prime chceck its family
I got result in 70 seconds but according to Project euler i should be able to
solve it under minute. I started to look at divisibility by 3. It can be shown that
our family must have at least 3 changing digits.
Also it can be shown that 4 digit is too much.
Looks like we need to check numbers that have 3k same digits and since we want smallest family
we can start with just 3 digits."""
n = 15*10**5
numbers = [True]*n
primes = []
for i in range(2,n):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j] = False
primes3 = []
for i in primes:
    array = [0 for x in range(10)]
    for c in str(i):
        array[int(c)] += 1
    for j in range(10):
        if array[j] == 3:
            primes3.append([i,j]) #i will store which number is 3 times in original number
for i in primes3:
    n = i[0]
    repeated_digit = i[1]
    start = 0
    if str(n)[0] == str(repeated_digit):
        start = 1
    family = 0
    for d in range(start,10):
        m = str(n)
        m = m.replace(str(repeated_digit),str(d))
        if numbers[int(m)]:
            family += 1
    if family == 8:
        print(i[0])
        break
        

    
