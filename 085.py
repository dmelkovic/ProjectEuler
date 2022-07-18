"""
its easy to determine number of all rectangles.
To determine rectangle we need to pick 2 different points on grid
Let the grid be size of m x n.
First point. (m+1)*(n+1)
With firs point we removed one line in horizontal and vertical direction.
Now we have only n*m possibilities to pick second point.
Hovewer there are multiple possibilities to pick same rectangle.
We need to divide by 4(2 diagonals)
"""
target = 2*10**6
error = target
best_area = 0
for m in range(1, target):
    for n in range(m, target):
        if abs(target-(m+1)*(n+1)*m*n//4 ) < error:
            error = abs(target-(m+1)*(n+1)*m*n//4 )
            best_area = m*n
        if (m+1)*(n+1)*m*n//4 > target:
            break
print(best_area)
