#isnt hard problem. For optimalisation we could store numbers and
#number of stepst to save some computing
def is_palindrome(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True
def is_Lychrel(n):
    s = 1
    m = int(str(n)[::-1])
    while not is_palindrome(n+m):
        n = n+m
        m = int(str(n)[::-1])
        s += 1
        if s == 50:
            return False
    return True
result = 0
for i in range(10000):
    if not is_Lychrel(i):
        result += 1
print(result)
