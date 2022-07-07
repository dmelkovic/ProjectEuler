n = 10**6  #estimation that primes up to milion will be enough
numbers = [True]*n
numbers[1] = False #1 is not prime and it can lead to incorret result 
primes = []
for i in range(2,n):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j] = False
def truncatable(n, right_to_left):
    global numbers
    n = str(n)
    while len(n)>1:
        if right_to_left:
            n = n[:-1]
        else:
            n = n[1:]
        if not numbers[int(n)]:
            return False
    return True
special_primes = []
for i in range(len(primes)-1,3,-1):
    if truncatable(primes[i], True) and truncatable(primes[i], False):
        special_primes.append(primes[i])
print(sum(special_primes))
