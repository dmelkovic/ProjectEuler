primes = [2,3,5,7,11,13,17,19]
result = 1
for i in primes:
    y=1
    while i**y<=20:
        y+=1
    y-=1
    result*=i**y
print(result)
