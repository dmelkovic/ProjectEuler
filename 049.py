def perm(a):
    p=[]
    if len(a)==1:
        return [a]
    elif len(a)==2:
        return [a[0]+a[1],a[1]+a[0]]
    for i in range(0,len(a)):
        c=a[i]
        a1=a[0:i]
        a2=a[i+1::]
        b=a1+a2
        for j in perm(b):
            p.append(c+j)
    return p

n = 10000
numbers = [True]*n
primes = []
for i in range(2,n):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j] = False
for i in range(primes.index(1487)+1,len(primes)):
    for j in range(i+1,len(primes)):
        k = (primes[j]-primes[i])*2+primes[i]      #aritmetic sequence
        if k<10000:
            if numbers[k]:
                permutations = perm(str(primes[i]))
                if str(primes[j]) in permutations and str(k) in permutations:
                    print(str(primes[i]) + str(primes[j]) + str(k) )
