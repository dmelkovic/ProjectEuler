import itertools
s = [0,1,2,3,4,5,6,7,8,9]
permutations = list(itertools.permutations(s))
permutations.sort()
result = ""
for x in permutations[10**6-1]:
    result += str(x)
print(result)
