a = 1 #first term of FS
b = 1 #second term of FS
index = 2
while len(str(b)) != 1000:
    a,b = b, a+b
    index += 1
print(index)
