#You are given three numbers representing heights.
#👉 Check:
# If middle number is greater than both → print "Peak"
#If middle number is smaller than both → print "Valley"

a=int(input("enyer the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if b>a and b:
	print("peak")
elif b<a and b:
	print("valley")
else:
	print("slope")