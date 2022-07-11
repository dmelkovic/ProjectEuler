"""there is pretty straightforward rule.
lets look at denominators. next denominator is sum of current
denominator and numerator.
Similarly numerator – next numerator is 2 times current + previous is next
"""
result = 0
expansion = 2
n1 = 3
d1 = 2
n2 = 7
d2 = 5
while expansion < 1000:
    n1, d1, n2, d2 = n2, d2, 2*n2+n1, n2+d2
    if len(str(n2)) > len(str(d2)):
        result += 1
    expansion += 1
print(result)

