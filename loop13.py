#Count how many times a digit appears in a number
a=int(input("enyer the number"))
digit=int(input("enter the digit"))
count=0
while a>0:
	value=a%10
	if value==digit:
	     count+=1
	a=a//10
print("digit repeated",count,"times")