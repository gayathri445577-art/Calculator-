#Take:
#Operator (+, -, *, /)
#Use match to perform operation between two numbers.
g=(input("enter the operator"))
a=int(input("enter the number"))
b=int(input("enter the number"))
match g:
	case "+":
		print("added",a+b)
	case "-":
		print("substract",a-b)
	case "*":
		print("multiplication",a*b)
	case "/":
		print("division",a/b)
	case _:print("invalid")