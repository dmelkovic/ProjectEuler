s=0
jednotky=["","one","two","three","four","five","six","seven","eight","nine"]
teen=["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
desiatky=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
tisic="thousand"
sto="hundred"
for i in range(1,1001):
    p=0
    if i//1000>0:
        p=p+len(jednotky[i//1000])+len(tisic)
    if i//100>0 and i<1000:
        p=p+len(jednotky[(i%1000)//100])+len(sto)
    if i%100>0 and i//100>0:
        p=p+3
    if i%100>10 and i%100<20:
        p=p+len(teen[i%100-10])
    else:
        p=p+len(desiatky[i%100//10])+len(jednotky[i%10])
    s=s+p
print(s)
