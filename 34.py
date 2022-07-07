#9! is about 4*10^5. At some point number will be bigger than sum factorial digit
# x*10^4 = 10^x-1 where x is number of digits
# we can see that 6 digit should be enough
s = 1
factorial = [1]
for i in range(1,10):
    s *= i
    factorial.append(s)

def digit_factorial(n):
    global factorial
    s = 0
    for c in str(n):
        s += factorial[int(c)]
        if s>n:
            return False
    if s==n:
        return True
    return False
total = 0
for i in range(3,25*10**5):
    if digit_factorial(i):
        total += i
print(total)
