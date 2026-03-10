#write a program to pop all elements from stack using  while loop until stack is empty
stack = []
while True:
    element = input("Enter element (type 'stop' to finish adding): ")
    if element == "stop":
        break
    stack.append(element)
print("Stack is:", stack)
while len(stack) > 0:
    e = stack.pop()
    print("Removed element:", e)
    print("Stack now:", stack)
print("Stack is empty")