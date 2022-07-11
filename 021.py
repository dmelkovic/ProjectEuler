n = 10000
s = 0
divisors = [1]*(n+1)
for i in range(2,n):
    for j in range(2*i,n,i):
        divisors[j] += i
for a  in range(1,n+1):
    for b in range(a+1,n+1):
        if divisors[a]==b and divisors[b]==a:
            s += a+b
print(s)
