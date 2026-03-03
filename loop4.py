#Print all even numbers and odd numbers between 1 to 50.
a=1
even_count=0
odd_count=0
while a<=50:
	if a%2!=0:
	     odd_count+=1
	     print(a)
	else:
		even_count+=1
		print(a)
	a+=1
print(" total even count",even_count)
print("total odd count",odd_count)