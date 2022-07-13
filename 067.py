"""I reused my core from problem 018. I just needed to implement pyramid from file"""
pyramid = []
with open("p067_triangle.txt", "r") as file:
    lines = file.read()
    lines = lines.split("\n")
    lines = lines[:-1]
    for line in lines:
        pyramid.append(line.split(" "))
rows = len(pyramid)
# we will go from bottom to top
for row in range(rows-2,-1,-1):
    for i in range(row+1):
        pyramid[row][i] = int(pyramid[row][i]) + max(int(pyramid[row+1][i]), int(pyramid[row+1][i+1]))
print(pyramid[0][0])    
        
