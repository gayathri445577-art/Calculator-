#Find Sum of odd Numbers Between 1 and N
i=1
count=0
sum=0
while i<=20:
	if i%2!=0:
		count+=1
		print(i)
	sum=sum+i
	i+=1
print("sum is",sum)
print("total count",count)