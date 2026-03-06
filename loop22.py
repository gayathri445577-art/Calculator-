#Write a program using a while loop to find the product of all digits in a number.
a=int(input("enter the number"))
sum=1
count=0
while a>0:
	c=a%10
	sum=sum*c
	count+=1
	a=a//10
print("the peoduct of a is",sum)
print("the count of the numbers",count)