"""
https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
"""
def gcd(a,b):
    while a!=0:
        if a>b:
            a=a%b
        else:
            a,b=b,a
    return b

l = 1500000
result = 0
triangles = [0]*(l+1)
for m in range(2, int(l**.5)):
    for n in range(1,m):
        if gcd(m,n) == 1 and (m+n)%2==1:
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            if a+b+c<=l:    #just to be sure that it can fit into array
                j=1
                while j*(a+b+c) <= l:
                    triangles[j*(a+b+c)]+=1
                    j=j+1
            else:
                break
for i in range(0,l+1): 
    if triangles[i] == 1:
        result += 1
print(result)
