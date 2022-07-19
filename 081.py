"""
i started solving matrix from end. If im in right column or bottom row
i had only one option to reach end. In the row and the colum every tile
is equal sum to reach end. Now we can work with submatrix n-1xn-1.
Starting at bottom right i can choose which sum sum is beter for me.
Meaning is better to go down or right. This principle will aplly to any
tile which is touching 2 already computed tiles. I decidet to go by lines
from bottom to top
"""
with open("p081_matrix.txt", "r") as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        a = list(map(int, line.split(',')))
        matrix.append(a)

n = len(matrix)
for i in range(n-2,-1,-1):
    matrix[n-1][i] += matrix[n-1][i+1]
    matrix[i][n-1] += matrix[i+1][n-1]
for i in range(n-2,-1,-1):
    for j in range(n-2,-1,-1):
        matrix[i][j] += min(matrix[i+1][j], matrix[i][j+1])
print(matrix[0][0])
