#sounds great to implement recursive function
n = 10**6
chains = {1: 1}
def collatz(n):
    global chains
    if n in chains:
        return chains[n]
    if n%2==0:
        chains[n] = 1 + collatz(n//2)
    else:
        chains[n] = 2 + collatz((3*n+1)//2)
    return chains[n]
longest = 0
number = 0
for i in range(1,n):
    if collatz(i) > longest:
        longest = collatz(i)
        number = i
print(number)
