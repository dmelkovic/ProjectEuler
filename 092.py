"""
bruteforce is extremly slow. I realized that nubes will reduce drasticly.
That mean i need to compute around 600 numbers
Worst case 7*9^2 = 567. Then i will be able to tell if nuber ends on89 or 1
after first iteration

"""
d = {str(x):x*x for x in range(10)}
def next_number(c):
    c_new = 0
    for j in str(c):
        c_new += d[j]
    return c_new
limit = 9*9*7+1
n = 10**7
numbers = [i for i in range(limit)]
s=0
for i in range(1,n+1):
    c = i
    if i < limit:
        while c != 1 and c != 89:
            c = next_number(c)
        numbers[i] = c
    else:
        c = numbers[next_number(i)]
    if c == 89:
        s += 1
print(s)
