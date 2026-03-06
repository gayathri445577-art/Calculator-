#Write a program using a while loop to find the sum of digits in a number and count.
a=int(input("enter the number"))
sum=0
count=0
while a>0:
	c=a%10
	sum=sum+c
	count+=1
	a=a//10
print("the sum of a is",sum)
print("the count of the numbers",count)