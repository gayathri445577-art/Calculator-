#You are given row r and column c
#Check:
#If r == c
#If r is even → print "Even Diagonal"
#Else → print "Odd Diagonal"
#Else → print "Not Diagonal"

b=int(input("enter the rows"))
c=int(input("enter the columns"))
if b==c:
	if b%2==0:
		print("even diagonal")
	else:
		print("odd diagonal")
else:
	print("not diagonal")