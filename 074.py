"""
I precomputed 0-9 factorials because we will use them a lot.
Also i made function next_number which returns next factorial digit number.
This programs goes through evety integer 1, 10^6 and starts doing chain.
It breaks if i get to number which chain lenght is stored or when i get
number which is made it chain.
"""
factorials = [1]
s = 1
for i in range(1,10):
    s *= i
    factorials.append(s)

def next_number(m):
    global factorials
    m_new = 0
    for digit in str(m):
        m_new += factorials[int(digit)]
    return m_new

chains = {}
n = 10**6
for i in range(1,n):
    number = i
    chain = []
    l = 0
    while number not in chain and number not in chains:
        chain.append(number)
        number = next_number(number)
        l += 1
    if number not in chains:
        chain.append(number)
        chain.reverse()
        if chain[-1] == chain[0]:
            chains[chain[0]] = l
        while chain[-1] != chain[0]:
            chains[chain[-1]] = l
            l -= 1
            chain.pop()
    else:
        for j in chain:
            chains[j] = l + chains[number]
            l -= 1
result = 0
for i in range(1,n):
    if chains[i] == 60:
        result += 1
print(result)
