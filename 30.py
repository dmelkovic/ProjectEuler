#x9^5=10^x-1
# x*10^5 = 10^x
#looks like it makes sence to try up to 6 digit numbers
s = 0
for i in range(2,10**6):
    n = 0
    for j in str(i):
        n += int(j)**5
    if n==i:
        s += i
print(s)
