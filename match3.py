#Take a number (1–7) and print:
#Weekday → 1 to 5
#Weekend → 6,7
#Invalid → others
a=int(input("enter the number"))
match a:
	case 1| 2| 3| 4| 5:
		print("weekday")
	case 6 | 7 :
		print("it is the weekend")
	case _:
		print("invalid")