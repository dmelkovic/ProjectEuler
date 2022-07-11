def number_of_divisors(n):
    primes = []
    powers = []
    d = 2
    c = 0
    while n!=1:
        if n%d==0:
            c+=1
            n=n//d
        else:
            primes.append(d)
            powers.append(c)
            d+=1
            c=0
    primes.append(d)
    powers.append(c)
    #print(powers)
    product = 1
    for i in powers:
        if i!=0:
            product*=(i+1)
    return product
n=1
while number_of_divisors(n*(n+1)//2)<500:
    n+=1
print(n*(n+1)//2)
