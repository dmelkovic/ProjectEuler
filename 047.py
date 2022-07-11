#basicly ist prime sieve but instead of True/False
#we will add 1 to every multiple of prime
n = 2*10**6
factors = [0]*n
for i in range(2,n):
    if factors[i] == 0:
        for j in range(i+i,n,i):
            factors[j] += 1 
c = 0
for i in range(2,n):
    if factors[i] == 4:
        c += 1
    else:
        c = 0
    if c == 4:
        print(i-3) #i is 4th i-1 is 3rd ... i-3 is first
        break
