#Write a program using a while loop to check whether the digits of a number are in ascending order.
a = int(input("enter the number"))
prev = 10
flag = True
while a > 0:
    digit = a % 10   
    if digit > prev:
        flag = False
        break     
    prev = digit
    a = a // 10
if flag:
    print("Ascending order")
else:
    print("Not ascending")