def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result


number = factorial(100)
s = 0
for i in str(number):
    s += int(i)
print(s)
