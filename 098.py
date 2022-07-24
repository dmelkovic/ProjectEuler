"""
It seems a lot to campare 2000 words with each other. If 2 words are anagrams
they will have same amout of letters. Thats why I made groups of words
with same lenght and then check if 2 words have same letters.
If yes they form anagramic pair. I did replacing digits using squares
I filtered squares as well. For each square equal in lenght with anagrams
I paired letter with numbers. Check for errors in first word. Then i replaced
digits in second word and checked if that is square. If yes i return highest of those 2.
"""
squares = [x*x for x in range(10**5)]
square_groups = [[] for x in range(10+1)]
squares = set(squares)

for i in squares:
    square_groups[len(str(i))].append(i)

def same_letters(a,b):
    a, b = list(a), list(b)
    a.sort()
    b.sort()
    if a == b:
        return True
    return False
def anagram_to_number(a,b, letters, i):
    global squares
    d = {}
    i = str(i)
    digits = set()
    for x in range(len(a)):
        if a[x] not in d:
            if i[x] not in digits:
                d[a[x]] = i[x]
                digits.add(i[x])
            else:   #we would use same digit multiple times
                return -1
        else: #if used digits in dictionary is not equal
            if d[a[x]] != i[x]:
                return -1
    b2 = ""
    for x in range(len(b)):
        b2 += d[b[x]]
    if int(b2) in squares and b2[0] != "0":
        return max(int(b2),int(i))
    return -1


def anagramic_square(a,b):
    numbers = set([x for x in range(0,10)])
    letters = list(set(list(a)))
    n = len(a)
    highest = 0
    for i in square_groups[n]:
        highest = max(anagram_to_number(a,b, letters, i), highest)
    return highest

with open("p098_words.txt", "r") as file:
    text = file.read()
    text = text.replace('"',"")
    words = text.split(",")
groups = [[] for x in range(20)]
for word in words:
    groups[len(word)].append(word)

pairs = []
for i in range(len(groups)):
    if len(groups[i]) > 0:
        for a in range(len(groups[i])):
            for b in range(a+1,len(groups[i])):
                if same_letters(groups[i][a], groups[i][b]):
                    pairs.append([groups[i][a], groups[i][b]])
result = 0
for pair in pairs:
    result = max(result, anagramic_square(pair[0], pair[1]))
print(result)
