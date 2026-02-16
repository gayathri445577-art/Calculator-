m=70
p=75
s=89
a=54
d=95
average = (m+ p + s+ a + d) / 5
print("averagemarks",average)
if average >= 75 and m>= 50 and p >= 50 and s>= 50 and a >= 50 and d>= 50:
    print("Distinction")

elif average >= 60 and m>= 40 and p>= 40 and s>= 40 and a>= 40 and d>= 40:
    print("First Class")

elif average >= 40:
    print("Pass")

else:
    print("Fail")