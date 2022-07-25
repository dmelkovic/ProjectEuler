"""
We can generate from 0 to our goal number.
0 is possible to obtain only in 1 way.
I will use coin analogy.
if we know number of x-c ways, where x is value and c is "coin"
then x is obtainable same amount ways as x-c.
If we go trough all c values we cangenerate number of ways of n and
also all numbers less than n

"""
n = 100 + 1
number_of_ways = [0]*n
numbers = [x for x in range(1,n-1)]
number_of_ways[0] = 1
for i in numbers:
    for j in range(i,n):
        number_of_ways[j] += number_of_ways[j-i]
print(number_of_ways[100])
