"""
With combinations it was easy. I generated all possible tuples of size 6
with digits using 0-9 digits. Then i added 6 or 9 if other one was already there.
I checked numbers i can get.
"""
import itertools
s = "0123456789"
l = list(itertools.combinations(s, 6))
squares = [(2-len(str(x*x)))*"0"+str(x*x) for x in range(1,10)]
def check(cube1, cube2):
    global squares
    cube1 = set(cube1)
    cube2 = set(cube2)
    if "6" in cube1:
        cube1.add("9")
    if "6" in cube2:
        cube2.add("9")
    if "9" in cube1:
        cube1.add("6")
    if "9" in cube2:
        cube2.add("6")
    check_array = [False]*9 
    for i in range(len(squares)):
        digit1 = squares[i][0]
        digit2 = squares[i][1]
        if digit1 in cube1 and digit2 in cube2:
            check_array[i] = True
        if digit2 in cube1 and digit1 in cube2:
            check_array[i] = True
    if check_array == [True]*9:
        return True
    return False
solutions = []
for i in range(len(l)):
    for j in range(i,len(l)):
        if check(l[i], l[j]):
            if [l[i], l[j]] not in solutions:
                solutions.append([l[i], l[j]])
print(len(solutions))
