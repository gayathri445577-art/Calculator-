#count vowels in a string
a= input("enter a string")
b="aeiou"
count=0
for i in a:
	if i in b:
		count+=1
		print("vowels are:",i)
print("count is",count)
