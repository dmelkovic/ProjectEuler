"""
Thanks to wikipedia i solve this
https://en.wikipedia.org/wiki/Partition_function_(number_theory)
There is nice recursive function to compute partitions.
I thought using Ramanujan's congruences but then I realized
i would need to compute all partition anyways
"""
partitions = [1]
n = 1
while True:
    i = 1
    p = 1
    partitions.append(0)
    while p <= n:
        if (i+1)%4>1: sign = 1
        else: sign = -1
        partitions[n] += sign*partitions[n-p]
        partitions[n] = partitions[n] % 10**6
        
        i += 1
        if i%2 == 0:
            j = -i//2
        else:
            j = (i+1)//2
        p = j*(3*j-1)//2
    if partitions[n] == 0:
        print(n)
        break
    n += 1
