a=int(input("enter the number"))
b=int(input("enter the number"))
op=input("enter the operator").strip( )
if op=='+':
	print(a+b)
elif op=='-':
	print(a-b)
elif op=='*':
	print(a*b)
elif op=='/':
	print(a/b)
else:
	print("others")