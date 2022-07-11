"""i^n has n digit when 10^(n-1)<= i^n < 10^n
lets use logarithms to see what i should be
10^n/10 <= i^n
i^n < 10^n -> clearly i can be only {1,...,9}
------------------
nlog(10)-log(10) < n*log(i)
nlog(10)-nlog(i) < log(10)
n[log(10)-log(i)]< log(10)
n < log(10)/[log(10)-log(i)]
"""
result = 0
from math import log
for i in range(1,10):
    result += int( log(10)/(log(10)-log(i)) )
print(result)
