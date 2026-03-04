#Find Product of Digits
a=int(input("enter the number"))
product=1
while a>0:
	digit=a%10
	product=product*digit
	a=a//10
print("the product is",product)