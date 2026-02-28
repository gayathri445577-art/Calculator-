#Take a number and classify it as:
#Single digit
#Two digit
#Three digit
#Large number
#Using match
a=input("enter a number").strip( )
digit=len(str(a))
match digit:
	case 1:
		print(" it is single digit")
	case 2:
		print("it is double digit")
	case 3:
		print("it is threable digit")