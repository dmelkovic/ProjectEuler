"""
Technicly bruteforced. I sieved primes up to 10000 and then try every
combination less than 5*10^7 and added them to set. 
"""
l = 10**4
maximum = 5*10**7
numbers = [True]*l
primes = []
solutions = set()
s=0

for i in range(2,l):
    if numbers[i]==True:
        primes.append(i)
        for j in range(i*i,l,i):
            numbers[j]=False

for c in range(0,len(primes)):
    for b in range(0,len(primes)):
        for a in range(0,len(primes)):
            if primes[c]**2+primes[b]**3+primes[a]**4<maximum:
                solutions.add(primes[c]**2 + primes[b]**3 + primes[a]**4)
            else:
                break
print(len(solutions))
