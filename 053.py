"""I was thinking about using properties of pascal triangle...
For eaxmple once we found element that is > 10^6
then we know elements in row bigger than 10^6 thanks to the symetry.
But python is python and compute 100 rows is quite fast."""
from math import comb
result = 0
for i in range(2, 101):
    for j in range(2, i):
        if comb(i, j) > 1000000:
            result += 1
print(result)
