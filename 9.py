for a in range(1,500):
    for b in range(a,1000-a):
        c = 1000-a-b
        #we dont know if a,b or c will be largest so wi will do little trick
        m = max(a,b,c)
        if a*a + b*b + c*c - 2*m*m == 0:
            print(a*b*c)
            break
