n = 28123 + 1
numbers = [False]*n
divisors = [1]*n

#find sum of proper divisors
for i in range(2,n):
    for j in range(2*i,n,i):
        divisors[j]+=i

abundant = []
#get abundant numbers
for i in range(2,n):
    if divisors[i]>i:
        abundant.append(i)

#mark numbers that can be obtained as sum of 2 abundant numbers
for a in range(len(abundant)):
    for b in range(a, len(abundant)):
        if abundant[a]+abundant[b] < n:
            numbers[abundant[a]+abundant[b]] = True
s = 0
for i in range(1,n):
    if not numbers[i]:
        s += i
print(s)
