def digitsum(n):
    n = str(n)
    s = 0
    for c in n:
        s += int(c)
    return s

maxsum = 0
for a in range(1,100): 
        for b in range (1,100):
                s = digitsum(a**b)
                maxsum = max(s,maxsum)
print(maxsum)
