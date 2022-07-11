def is_triangle(word):
    s = 0
    for c in word:
        s += ord(c)-ord("A")+1
    #n*n+n-2s=
    #D=1+8s
    n = (-1+(1+8*s)**.5)/2
    if int(n) == n:
        return True
    return False
result = 0
with open("p042_words.txt", "r") as file:
    text = file.read()
    text = text.replace('"',"")
    words = text.split(",")
    for word in words:
        if is_triangle(word):
            result += 1
print(result)
