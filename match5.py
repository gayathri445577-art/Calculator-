#Input grade letter:
g=input("enter the grade").strip( )
match g:
	case 'A' | 'B':
		print("excellent")
	case 'C':
		print("good")
	case 'D':
		print("pass")
	case 'E':
		print("fail")
	case _:
		print("invalid")
