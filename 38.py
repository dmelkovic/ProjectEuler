def is_pandigital(n):
    n = set(str(n))
    if n == set([str(x) for x in range(1,10)]):
        return True
    return False
max_pandigital = 0
for i in range(2,10000):
    pandigital = ""
    j = 1
    while True:
        pandigital += str(i * j)
        if len(pandigital) > 9:
            break
        elif len(pandigital) == 9:
            if is_pandigital(pandigital) and int(pandigital) > max_pandigital:
                max_pandigital = int(pandigital)
            break
        j += 1
print(max_pandigital)
