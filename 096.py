"""
Each sudoku is solved by backtracking. Its not fastest but works
"""
def empty(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col]== 0:
                l[0]= row
                l[1]= col
                return True
    return False

def in_row(grid, row, n):
    for i in range(9):
        if(grid[row][i] == n):
            return True
    return False

def in_col(grid, col, n):
    for i in range(9):
        if(grid[i][col] == n):
            return True
    return False
 
def in_box(grid, row, col, n):
    for i in range(3):
        for j in range(3):
            if grid[i + row][j + col] == n:
                return True
    return False

def is_safe(grid, row, col, n):
     return not in_row(grid, row, n) and not in_col(grid, col, n) and not in_box(grid, row - row % 3,col - col % 3, n)
           
def solve_sudoku(grid):
    l =[0, 0]
    if not empty(grid, l):
        return True
    row = l[0]
    col = l[1]
    for n in range(1, 10):
        if is_safe(grid,row, col, n):
            grid[row][col]= n
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0 
    return False
s=0
with open("p096_sudoku.txt", "r") as file:
    lines = file.readlines()
    n = len(lines)//10
    for i in range(0,n):
        grid=[]
        for j in range(0,9):
            l=[]
            for k in range(0,9):
                l.append(int(lines[i*10+j+1][k]))
            grid.append(l)
        if solve_sudoku(grid):
            s=s+int(100*grid[0][0]+10*grid[0][1]+grid[0][2])
print(s)
