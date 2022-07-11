import time
t1 = time.time()
global c
n = 10**4
numbers = [True]*n
primes = []
for i in range(2,n):
    if numbers[i]==True:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j]=False
def prime(n):
    global numbers
    if n==2: return True
    if n==3: return True
    if n%2==0: return False
    if n%3==0: return False
    if n<10: return True
    if n<10**4:
        return numbers[n]
    d=6
    while (d-1)<=n**.5:
        if n%(d+1)==0:
            return False
        if n%(d-1)==0:
            return False
        d+=6
    return True
def check(arr):
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                if prime(int(arr[i]+arr[j]))==False:
                    return False
    return True
result=[]
stop = False
for a in range(0,len(primes)):
    for b in range(a+1,len(primes)):
        if check([primes[a], primes[b]]):
            for c in range(b+1,len(primes)):
                if check([primes[a], primes[b], primes[c]]):
                    for d in range(c+1,len(primes)):
                        if check([primes[a], primes[b], primes[c], primes[d]]):
                            for e in range(d+1,len(primes)):
                                if check([primes[a], primes[b], primes[c], primes[d], primes[e]]):
                                    result=[primes[a], primes[b], primes[c], primes[d], primes[e]]
                                    stop = True
                                    break
                            if stop: break
                    if stop: break
            if stop: break
    if stop: break
t2 = time.time()
print(result, sum(result))
print(t2-t1)
