#implement stack using list , perform pop and push by using while loop
stack = []
n=int(input("how many elements added"))
i = 0
while i < n:
    element = input("Enter element: ")
    stack.append(element)
    i += 1
print("Stack is:", stack)
e = stack.pop( 0)
print("Removed element is:", e)
print("Stack after pop:", stack)