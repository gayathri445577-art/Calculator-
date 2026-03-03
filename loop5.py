#Reverse a number using while loop.
i=int(input("enyer the number"))
new_reverse=0
while i>0:
	last_digit=i%10
	new_reverse=new_reverse*10+last_digit
	i=i//10
print(new_reverse)