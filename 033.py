fractions = []
for n in range(10,100):
    for d in range(n+1,100):
        for i in range(2):
            for j in range(2):
                numerator = str(n)
                denominator = str(d)
                if numerator[i] == denominator[j] and numerator[i] != "0":
                    numerator = numerator[1-i:2-i]  #for 0 will give second position, for 1 first
                    denominator = denominator[1-j:2-j]
                    if n*int(denominator) == int(numerator)*d:
                        fractions.append([n,d])
print(fractions)
n = 1
d = 1
for i in fractions:
    n *= i[0]
    d *= i[1]
i = 2
while i <= n:
    if n%i==0 and d%i==0:
        n = n//i
        d = d//i
    else:
        i+=1
print(d)
