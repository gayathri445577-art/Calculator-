#reverse list with using reverse() in while loop
a=[ ]
s=int(input("how many elements are given"))
i=0
while i<s:
	b=input("enter elements")
	a.append(b)
	i+=1
c=list(reversed(a))
print("the list is:",a)
print("reverse list is:",c)