"""
worst scenario is 1 to 9 pandigal prime.
With sieve we would need to go through array with size 10**9. Thats a lot
Its better to go by permutation of 1..n where n will be rising to 9.
Its for sure better. 1!+2!+...+9! < 9*9! < 10^9 
"""
def permutation(a):
    p = []
    if len(a) == 1:
        return [a]
    elif len(a)==2:
        return [a[0]+a[1],a[1]+a[0]]
    for i in range(0,len(a)):
        c=a[i]
        a1=a[0:i]
        a2=a[i+1::]
        b=a1+a2
        for j in permutation(b):
            p.append(c+j)
    return p
def is_prime(n):
    if i == 1: return False
    if n==2: return True
    if n==3: return True
    if n%2==0: return False
    if n%3==0: return False
    if n<10: return True
    d=6
    while d<=n**.5:
        if n%(d+1)==0:
            return False
        if n%(d-1)==0:
            return False
        d+=6
    return True
s = ""
max_pandigital = 0
for i in range(1,10):
    s += str(i)
    for j in permutation(s):
        if is_prime(int(j)) and int(j)>max_pandigital:
            max_pandigital = int(j)
print(max_pandigital)
