#http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf
result = 0
s=0
for i in range(2,100):
    a = 5*i
    b = 5
    if int(i**.5)**2 != i: #continue only if number is not square – will have decimal digits
        while len(str(b))<105:
            if a >= b:
                a -= b
                b += 10
            else:
                a *= 100
                b = (b-5)*10 + 5
        p = 0
        c = str(b)[:100]
        for j in c:
            p = p+int(j)
        result += p
print(result)
        
