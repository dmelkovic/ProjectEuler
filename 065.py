"""by looking at the sequence i found some properties
for next term. Note that sum of numerators is next numerator.
similarly denominator. after 3 term something intresting happens.
Instead of adding 2 terms together
we need to take (i//3*2) times + previous to get next one"""
i = 4
n1 = 3
d1 = 1
n2 = 8
d2 = 3
while i <= 100:
    if i%3==0:
        n1 ,d1 , n2, d2 = n2, d2, n1+(i//3*2)*n2, d1+(i//3*2)*d2
    else:
        n1 ,d1 , n2, d2 = n2, d2, n1+n2, d1+d2
    i+=1
result = 0
for i in str(n2):
    result += int(i)
print(result)
