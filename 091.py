"""
I wanted to split problem for subproblems.
I realized that i can do according to right angle
If right angle is at 0 we have 50*50 posibilities.
Otherwise let right angle be at x1, y1 - we will check pythagorean theorem
If x2.y1 - y2x1 = 0 than we have 0 area.
"""
n = 50
result = 0
for x1 in range(0,n+1):
    for x2 in range(0,n+1):
        for y1 in range(0,n+1):
            for y2 in range(0,n+1):
                if x2*y1-y2*x1 != 0:
                    if x1*(x1-x2) + y1*(y1-y2) == 0:
                        result += 1
print(result + n*n)
