#Given a list of numbers, count how many are even and how many are odd.
num= [3, 8, 5, 12, 7, 10,8,45,64]
even=0
odd=0
for  x in num:
	if x%2==0:
		print("even number is :",x)
		even+=1
	else:
   	  print("odd number is :",x)
   	  odd+=1
		