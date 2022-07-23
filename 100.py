"""diophantine equation(quadratic)
2*b*(b-1) = n*(n-1)
2b^2 - 2b -n^2 + n = 0
used http://www.numbertheory.org/php/generalquadratic.php for recuring formula
"""
b = 15
n = 21
t = 10**12
 
while n < t:
    b1 = 3*b + 2*n - 2
    n1 = 4*b + 3*n - 3
    b, n = b1, n1
print(b)
