#Check whether a number is multiple of 3 or 7.
a=int(input("enter the number"))
if a%3==0:
	print("divisible by 3")
elif a%7==0:
	print("divisible by 7")
else:
	print(" does not divisible by 3 and 7")