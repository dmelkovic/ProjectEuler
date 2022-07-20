"""
I removed multiple records. Then i got all digits which are in the attemps
It was only 33 atempts and 8 digits. We wanted shortest possible so it should
contain each digit once(ideally).
Thats why i made all permutations and bruteforced through them
"""
from itertools import permutations
def check(password):
    n = len(password)
    global attempts
    for i in attempts:
        pointer = 0
        for j in range(n):
            if password[j] == i[pointer]:
                pointer += 1
            if pointer == 3:
                break
        if pointer != 3:
            return False
    return True
with open("p079_keylog.txt", "r") as file:
    lines = file.read()
    lines = lines.split("\n")
    lines = lines[:-1]
    attempts = set()
    for i in lines:
        attempts.add(i)
    digits = set()
    for i in attempts:
        for j in i:
            digits.add(j)
    digits = list(digits)
permutations = list(permutations(digits))
for p in permutations:
    password="".join(x for x in p)
    if check(password):
        print(password)
