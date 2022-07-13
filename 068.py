"""
I think its good idea to solve this with backtracking
For me its easier when solutions will be array of lenght 10.
Pick external node which is 0 and go towards centre. Then pick external node
that overlaps with last node from first triplets and idex of its node will be smallest as possible.
Continue and you will enumerate every node.
"""
solutions = []
solution = []
solution_set = set(solution)
strings = []
def solve():
    global solution, solutions
    if len(solution)==10 and check(solution):
            if solution not in solutions:
                solutions.append(solution.copy())
    else:
        for i in range(1,11):
            if i not in solution_set:
                solution.append(i)
                solution_set.add(i)
                if check(solution):
                    solve()
                solution.pop()
                solution_set.remove(i)
def check(solution):
    #This function check if backtracking move is valid. I make also condition for not fully filled
    #triplets in to make program run faster.
    l = len(solution)
    if l==4:
        if sum(solution[:3]) < sum(solution[2:4]):
            return False
    elif l==5:
        if sum(solution[:3]) != sum(solution[2:5]):
            return False
    elif l==6:
        if sum(solution[2:5]) < sum(solution[4:6]):
            return False
    elif l==7:
        if sum(solution[2:5]) != sum(solution[4:7]):
            return False
    elif l==8:
        if sum(solution[4:7]) < sum(solution[6:8]):
            return False
    elif l==9:
        if sum(solution[4:7]) != sum(solution[6:9]):
            return False
    elif l==10:
        if sum(solution[6:9]) != sum(solution[8:])+solution[1]:
            return False
    else:
        return True
    return True

def solution_string(s):
    #in this function im rotating triplets so smallest external node is on the 1. place
    triplets_start = [s[0],s[3],s[5],s[7],s[9]]
    smallest_external = min(triplets_start)
    smallest_external_index = triplets_start.index(smallest_external)
    s = [str(x) for x in s]
    string_triplets = [ s[0]+s[1]+s[2] , s[3]+s[2]+s[4] , s[5]+s[4]+s[6] , s[7]+s[6]+s[8] , s[9]+s[8]+s[1] ]
    string_triplets =  string_triplets[smallest_external_index:] + string_triplets[:smallest_external_index]
    string = "".join(string_triplets)
    return string
solve()
for i in solutions:
    if solution_string(i) not in strings:
        strings.append(int(solution_string(i)))
maximum_string = 0
for i in strings:
    if len(str(i)) == 16:
        maximum_string = max(maximum_string, i)
print(maximum_string)
