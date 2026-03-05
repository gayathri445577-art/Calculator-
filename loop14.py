#Count how many times a digit appears in a number
a=int(input("enter the number"))
count={ } 
while a>0:
	value=a%10
	if value in count:
	    count[value]+=1
	else:
	 	count[value]=1
	a=a//10
print("digit repeated",count)