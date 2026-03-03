#Print all even numbers between 1 and 50.
i=1
count=0
while i<=50:
	if i%2==0:
	     count+=1
	     print(i)
	i+=1
print(" total count",count)