import math
"""
since this numbers are big and in great format i used log insted.
Then we can compare much smaller multiplication.
"""
best = [1,1] #base, exponent
line = -1
with open("p099_base_exp.txt", "r") as file:
    lines = file.readlines()
for i in range(0,len(lines)):
    r = lines[i]
    r = r.split(",")
    base = int(r[0])
    exponent = int(r[1])
    if exponent * math.log(base) > best[1] * math.log(best[0]):
        line = i
        best[0] = base
        best[1] = exponent
print(line+1)
    
