"""let n be size of spiral
numbers 1,9,25,... are obviously odd squares
similarly 1,5,17,... are close to even squares(exactly one more from them).
first diagonal is sum of n squares + n//2 = n*(n+1)*(2*n+1)//6 + n//2
 what about second diagonal. We can see, that 1+(4-1)+(9-2)+(16-3)+(25-4)
 This part of diagonal is sum of squares minus aritmetic sequence.
 We need to subtract 1 because it is on both diagonals"""
n = 1001
d1 = n*(n+1)*(2*n+1)//6 + n//2
d2 = n*(n+1)*(2*n+1)//6 - (n-1)*n//2
print(d1+d2-1)
