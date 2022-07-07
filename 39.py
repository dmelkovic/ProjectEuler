#we could generate pythagorean triplets but we just need perimeter up to 1000
#so we can simply bruteforce
triangles = [0]*1001
for a in range(1,500):
    for b in range(1, 500):
        c = int((a*a+b*b)**.5)
        if a+b+c<=1000:
            if a*a+b*b-c*c == 0:
                triangles[a+b+c] += 1
print(triangles.index(max(triangles)))
