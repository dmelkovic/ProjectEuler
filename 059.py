def mf(s): #most frequent
    return max(set(s), key = s.count) 
f = open("p059_cipher.txt", "r")
text=f.readline()
text=text.split(",")
c1=[]
c2=[]
c3=[]
for i in range(0,len(text)):
    text[i]=int(text[i])
    if i%3==0:
        c1.append(text[i])
    if i%3==1:
        c2.append(text[i])
    if i%3==2:
        c3.append(text[i])
print("most frequent char:",mf(c1),"|with percentage",100*c1.count(69)/len(c1),"|spacebar XOR most frequent is",32^69,"=", chr(101))
print("most frequent char:",mf(c2),"|with percentage",100*c2.count(88)/len(c2),"|spacebar XOR most frequent is",32^88,"=", chr(120))
print("most frequent char:",mf(c3),"|with percentage",100*c3.count(80)/len(c3),"|spacebar XOR most frequent is",32^80,"=", chr(112))
print("password is:",chr(101)+chr(120)+chr(112))
#spacebar is most probable character at any place. Thats why we take  XOR 32
def encode(t,p):
    et=[]
    for i in range(0,len(t)):
        et.append(chr(ord(p[i%3])^t[i]))
    print(''.join(et))
    return et
s=0
a=input("pswd:")
te=encode(text,a)
for i in range(0,len(te)):
    s=s+ord(te[i])
print(s)
        
