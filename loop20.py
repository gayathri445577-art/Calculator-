#Write a program using a while loop to find the sum of digits in a number.
a=int(input("enter the number"))
sum=0
while a>0:
	c=a%10
	sum=sum+c
	a=a//10
print("the sum of a is",sum)