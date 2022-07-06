with open("p022_names.txt", "r") as file:
    text = file.read()
    text = text.replace('"', '')
    names = text.split(",")
names.sort()
s = 0
for pos, name in enumerate(names):
    value = 0
    for c in name:
        value += ord(c)-ord("A")+1
    s += (pos+1)*value
print(s)
