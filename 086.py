"""
Best way to iamgine shortest path is to unfold cuboid.
distance will be sqrt( a^2 + (b+c)^2 )
1<a,b,c<=m. We can substitue bc = b+c. Then 2 <= bc <= 2*m and 1<= a <= m.
We can go through this options. There isnt much we can do about a,
but we can compute number of combinations of bc.
If bc<=m then b = 1, c=bc-1; .... b =bc-1, c= 1 leading to bc//2 solutions.
If bc>m value of b and c can be maximally m.
We will have solutions in form b=bc//2 c = bc/2; b=bc/2+1 c=bc/2-1...
b=bc/2+s=m c=bc/2-s. So number of solutions is roundup(bc/2)...m, both included.
m-roundup(bc/2)+1

"""
m = 2
s = 0
while s < 10**6:
    m += 1
    for bc in range(2,2*m+1):
        distance = (bc*bc+m*m)**.5 
        if distance == int(distance):
            if bc <= m:
                s += bc//2
            else:
                s += m-round(bc/2+0.5)+1
print(m)
            
        
        
