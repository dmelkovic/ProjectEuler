"""
I precomputed sum of proper divisor similarly to prime sieve.
Then it was easy to find chains. I looped chaining process until
i reached number above million or i found number already in chain
if first and last were equal its chain that returns to its original value.
I was thinking about storing some numbers but i wasnt so sure that would help.
Primes get to 1 and there are numbers which will lead above limit, But
on the way they could reach initial number. Its possible to store those
chains but i feel like it would be a lot of work for small improvement.
"""
import time
t1=time.time()
n = 10**6+1
numbers = [1]*n
for i in range(2,n//2):
    for j in range(2*i,n, i):
        numbers[j] += i
chains = {}
for i in range(1,n):
    number = i
    chain = []
    l = 0
    while number not in chain and number < n:
        chain.append(number)
        number = numbers[number]
        l += 1
    chain.append(number)
    if chain[0] == chain[-1] and len(chain)>1:
        chains[chain[0]] = l
max_value = 0
n_min = 0
for key, value in chains.items():
    if value > max_value:
        max_value = value
        n_min = key
t2 = time.time()
print(n_min)
print(t2-t1)
