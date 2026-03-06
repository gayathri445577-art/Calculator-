#Write a program using a while loop to print the number after removing the last digit each time.
a=654
print(a)
while a>0:
	c=a%10
	a=a//10
	print(a)
   