#Take a number n from the user and print the square of numbers from 1 to n.
a=int(input("enter the number"))
i=1
for i in range(1,a+1):
	i=i*i
print(a,"square is :",i)