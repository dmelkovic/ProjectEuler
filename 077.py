"""
This was similar to problem 76. Instead of using 1..n-1, we will use primes.
Felt like 1000 is enough for 5000 ways, then i used 100 instead
"""

n = 10**2
numbers = [True]*n
number_of_ways = [0]*n
primes = []

for i in range(2,n):
    if numbers[i]:
        primes.append(i)
        for j in range(i*i,n,i):
            numbers[j] = False
number_of_ways[0] = 1
for i in primes:
    for j in range(i,n):
        number_of_ways[j] += number_of_ways[j-i]
for i in range(len(number_of_ways)):
    if number_of_ways[i] > 5000:
        print(i)
        break
        
