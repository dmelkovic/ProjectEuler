def same_digits(x):
    digits = set(str(x))
    for i in range(2,7):
        if set(str(i*x)) != digits:
            return False
    return True
i = 1
while not same_digits(i):
    i += 1
print(i)
