coins = [1,2,5,10,20,50,100,200]
prize = 200
ways = [0]*(prize+1)
ways [0] = 1;
for i in range(8):
    for j in range(coins[i], prize+1):
        ways[j] = ways[j] + ways[j-coins[i]]
print(ways[200])
