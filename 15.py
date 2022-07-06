#we need to go both 20 blocks right and down, thus we need to do 40 moves
#imagine 40 digit number which codes our path. 1 means down, 0 right
#We need to pick 20 fortunate positions in our number which will have 1
import math
print(math.comb(40,20))
