#Check whether a triangle is:
#Equilateral
#Isosceles
#Scalen (Using 3 sides)
a= int(input("enter the first side"))
b=int(input("eneter the second sode"))
c=int(input("enyer the third side"))
if a==b==c:
	print("it is equilateral triangle")
elif a==b!=c:
	print("it is isoscels triangle")
elif a!=b!=c:
	print(" it is scalenes triangle")
else:
	print("it is not triangle")