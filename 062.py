"""this program is running through cubes and store string
containing information about number of each digits. Whenever it come
to string that is stored 5 times that is part of our cube family.
Than we will find smallest one from already stored."""
def digits(n):
    d = [0,0,0,0,0,0,0,0,0,0]
    for digit in str(n):
        d[int(digit)] += 1
    return "".join(str(x) for x in d)
i=1
memory = [0]
while True:
    a = i**3
    last_number = digits(a)
    memory.append(last_number)
    if memory.count(last_number) == 5:
        print( (memory.index(last_number))**3 )
        break
    i=i+1
    
