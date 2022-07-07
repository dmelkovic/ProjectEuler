def is_palindrome(s):
    s = str(s)
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
def binary(n):
    r = ""
    while n != 0:
        r += str(n%2)
        n = n//2
    return r[::-1]
n = 10**6
s = 0
for i in range(n):
    pass
    if is_palindrome(i):
        if is_palindrome(binary(i)):
            s += i
print(s)
