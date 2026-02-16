m=30
p=45
s=69
a=78
d=89
average = (m+ p + s+ a + d) / 5
print("averagemarks",average)
if average >= 75 and max(m,p,s,a,d)>=80:
    print("Distinction")

elif average >= 40 and min(m,p,a,s,d)<=60:
    print("First Class")

elif average >= 50:
    print("Pass")

else:
    print("Fail")