def perm(a):
    p=[]
    if len(a)==1:
        return [a]
    elif len(a)==2:
        return [a[0]+a[1],a[1]+a[0]]
    for i in range(0,len(a)):
        c=a[i]
        a1=a[0:i]
        a2=a[i+1::]
        b=a1+a2
        for j in perm(b):
            p.append(c+j)
    return p
result = 0
pandigals = perm("0123456789")
for i in pandigals:
    if int(i[1:4])%2==0:
        if int(i[2:5])%3==0:
            if int(i[3:6])%5==0:
                if int(i[4:7])%7 == 0:
                    if int(i[5:8])%11 == 0:
                        if int(i[6:9])%13 == 0:
                            if int(i[7:10])%17 == 0:
                                result += int(i)
print(result)
