a=int(input(" enter thw balance"))
b=int(input("enter the withdrawal amount"))
if b>a:
	print("insufficient funds")
elif a-b < 1000:
	print(" minimum balance violation")
else:
	print("transaction proved")