#match statement=
the match statement is used to perform compare the values on different actions or patterns and execute the matching block of statement.
#syntax=
match expression:
	case1:
		code
	case2:
		code ------
	case_:
		code
# it was i troduced in 3.10 version
#Multiple values in one case
the symbol is | (or) operator is ised
eg:
	day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
    