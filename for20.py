#Take a number n and find the sum of all odd numbers from 1 to n.
a=int(input("enter the number"))
sum=0
for i in range(1,a+1):
	if i%2!=0:
		sum=sum+i
		print(i,end="+")
print("=", sum)