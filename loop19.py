#Write a program using a while loop to find the factorial of a given number.
a=int(input("enter the number"))
fact=1
while a>=1:
	fact=a*fact
	a-=1
print("the factorial of  a is",fact)