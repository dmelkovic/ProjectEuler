def is_prime(n):
    if n==1: return False
    if n==2: return True
    if n==3: return True
    if n%2==0: return False
    if n%3==0: return False
    if n<10: return True
    d=6
    while (d-1)<=n**.5:
        if n%(d+1)==0:
            return False
        if n%(d-1)==0:
            return False
        d+=6
    return True

size = 1
step = 0
tile = 1
diagonals = 1
are_primes = 0
not_primes = 1
while are_primes/(are_primes+not_primes+1) > 0.1 or are_primes<1:
    tile += 2*size
    if is_prime(tile):
        are_primes += 1
    else:
        not_primes += 1
    step += 1
    if step == 4:
        step = 0
        size += 1
print(2*size+1)
