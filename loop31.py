#implement queue using list and remove elements by using while loop
queue=[ ]
a=int(input("entered the how many elements entered"))
i=0
while i<a:
	elements=input("enter the elements")
	queue.append(elements)
	i+=1
	print("the queue is",queue)
s=queue.pop(-3)
print("the removed element  is ",s)
print("the queue is",queue)