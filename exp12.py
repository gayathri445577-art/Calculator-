#Given a number n
#Check:
#If n is between 1–50
#If divisible by 5 → print "Low Multiple of 5"
#Else → print "Low Range"
#If n is between 51–100
#If divisible by 10 → print "High Multiple of 10"
#Else → print "High Range"
#Otherwise → print "Out of Range"

b=int(input("enter the number"))
if  1<=b <=50:
	if b%5:
		print("low multiples of 5")
	else:
		print("low range")
elif 51<=b<=100:
	if b%10:
		print("high multiples of 10")
	else:
		print("high range")
else:
	print("out of range")
	