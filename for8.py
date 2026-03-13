#Given a list of numbers, count how many are even and how many are odd.
a=[ ]
num=int(input("enter the how many numbers entered"))
even=0
odd=0
for  x in range(num):
	b=int(input("enter the numbers"))
	if b%2==0:
		print("even number is :",b)
		even+=1
	else:
   	  print("odd number is :",b)
   	  odd+=1
print("total even numbers",even)
print("total odd numbers",odd)