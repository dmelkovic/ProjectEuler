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
def p(n, k):
    if k==3: return n*(n+1)//2
    if k==4: return n*n
    if k==5:return n*(3*n-1)//2
    if k==6:return n*(2*n-1)
    if k==7:return n*(5*n-3)//2
    if k==8:return n*(3*n-2)
def inv_p(previous, k):
    start = int(str(previous)[-2:])
    if start < 10: return range(0,0)
    down = start*100
    up = down+99
    if k==3:    #n^2+n-2c=0
        xd = (-1+(1+8*down)**.5)/2
        xu = (-1+(1+8*up)**.5)/2
    if k==4:
        xd = down**.5
        xu = up**.5
    if k==5:
        xd = (1+(1+24*down)**.5)/6
        xu = (1+(1+24*up)**.5)/6
    if k==6:
        xd = (1+(1+8*down)**.5)/4
        xu = (1+(1+8*up)**.5)/4
    if k==7:
        xd = (3+(9+40*down)**.5)/10
        xu = (3+(9+40*up)**.5)/10
    return range(round(xd+.5),int(xu)+1)
a = 1
result = []
permutations = perm("34567")
while p(a,8)<10000:
    if p(a,8)>=1000:
        for k in permutations:
            for b in inv_p(p(a,8), int(k[0])):
                for c in inv_p(p(b,int(k[0])), int(k[1])):
                    for d in inv_p(p(c,int(k[1])), int(k[2])):
                        for e in inv_p(p(d,int(k[2])), int(k[3])):
                            for f in inv_p(p(e,int(k[3])), int(k[4])):
                                if str(p(f,int(k[4])))[-2:]==str(p(a,8))[:2]:
                                    result = [p(a,8),p(b,int(k[0])),p(c,int(k[1])),p(d,int(k[2])),p(e,int(k[3])),p(f,int(k[4]))]
                                    print(p(a,8),p(b,int(k[0])),p(c,int(k[1])),p(d,int(k[2])),p(e,int(k[3])),p(f,int(k[4])))
    a+=1
print(sum(result))
