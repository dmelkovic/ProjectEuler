n=1000
#sum of all multiples 3 and 5, but subtract multuples of 15
s3 = (n//3) * (n // 3 + 1) * 3 // 2
s5 = (n//5) * (n // 5 + 1) * 5 // 2
s15 = (n//15) * (n // 15 + 1) * 15 // 2
print(s3 + s5 - s15)
