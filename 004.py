def is_palindrome(n):
    n=str(n)
    for i in range(len(n)//2):
        if n[i]!=n[-i-1]:
            return False
    return True

largest = 0
for a in range(100,999):
    for b in range(a,999):
        if is_palindrome(a*b):
            largest = max(a*b,largest)
print(largest)
