"""phi(n) = n(1-1/p1)...(1-1/pk), where p1...pk are primes which divides n.
We can do alternation of sieve of eratosthenes to compute phi(n).
In the end we will find maximum."""
n = 10**6+1
phi = [x for x in range(n)]
for i in range(2,n):
    if i == phi[i]:     #found a prime
        for j in range(i,n,i):
            phi[j] = phi[j]*(i-1)//i
maximum_value = 0
maximum_i = 0
for i in range(2,n):
    if i/phi[i] > maximum_value:
        maximum_value = i/phi[i]
        maximum_i = i
print(maximum_i)
