#reverse list without using reverse() in while loop
a=[ 3,4,5,6]
i=0
j=len(a)-1
temp=0
while i<j:
	temp = a[i]
	a[i]=a[j]
	a[j]=temp
	i=i+1
	j=j-1
print("the list is:",a)