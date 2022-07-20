import itertools
"""
I manually written all combinations of parenthesis and operators.
Operators are - and numbers are x.
Then i iterate through all numbers and operators.
I made list of all permutations of chosen numbers and then I start
replace characters in the combinations. I used eval() to evalued expression
but i had to make exeption because there could be division by zero.
"""
x = ["x-x-x-x",
"(x-x)-x-x",
"x-x-(x-x)",
"x-(x-x)-x",
"(x-x)-(x-x)",

"(x-x-x)-x",
"((x-x)-x)-x",
"(x-(x-x))-x",

"x-(x-x-x)",
"x-(x-(x-x))",
"x-((x-x)-x)"]
longest = 0
res = [0,0,0,0]
op = ["+","-","*","/"]
p = [False for x in range(3025)] #=9*8*7*6+1
for a in range(1,10):
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                lis=p.copy()
                for o1 in range(4):
                    for o2 in range(4):
                        for o3 in range(4):
                            perm = list(itertools.permutations([a,b,c,d]))
                            for i in perm:
                                i = list(i)
                                for e in x:
                                    ex = str(e)
                                    ex = ex.replace("x",str(i[0]),1)
                                    ex = ex.replace("x",str(i[1]),1)
                                    ex = ex.replace("x",str(i[2]),1)
                                    ex = ex.replace("x",str(i[3]),1)
                                    ex = ex.replace("-",str(op[o1]),1)
                                    ex = ex.replace("-",str(op[o2]),1)
                                    ex = ex.replace("-",str(op[o3]),1)
                                    try:
                                        v = eval(ex)
                                    except ZeroDivisionError as err:
                                        v = 0.5
                                    if v == int(v):
                                        lis[int(v)]=True
                for i in range(1,len(lis)):
                    if lis[i] == False:
                        if i > longest:
                            longest = i
                            res = [a,b,c,d]
                        break
for i in res: print(i,end="")
