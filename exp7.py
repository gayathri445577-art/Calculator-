#check eletricity bill calculation
units=int(input("enter the units"))
if 0<= units<=100 :
   print("₹2/unit")
elif 101<=units<=200:
    print("₹3/unit")
elif 201<=units<=300 :
	print("₹5/unit")
else:
	print("300+ → ₹7/unit")