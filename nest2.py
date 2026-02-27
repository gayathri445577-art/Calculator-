#Check:
#If age ≥ 18
#If age ≥ 60 → Senior Ticket
#Else → Adult Ticket
#Else
#If age ≥ 5 → Child Ticket
#Else → Free Entry
	
age = int(input("enter the age: "))
if age >= 18:
    if age >= 60:
        print("Senior Ticket")
    else:
        print("Adult Ticket")
else:
    if age >= 5:
        print("Child Ticket")
    else:
        print("Free Entry")