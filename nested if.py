#Nested if and elif  statements
#nested if=the if statement inside another if                             statement
#elif=elif means "else if "it is used more than                          two if statements
#check of a number is postive and even
a=int(input("enter the number"))
if a > 0:
	print("it is positive number")
	if a%2==0 :
		  print("it is even number")
	else:
		  print("it is odd")
elif a<0:
	print("it is negative number")
else:
	print(" it is zero")