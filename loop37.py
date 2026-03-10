#write a program to find maximum element in list using while loop
a = list(map(int, input("enter numbers: ").split()))
while len(a) > 0:
    c = min(a)
    break
print("the minimum element is", c)