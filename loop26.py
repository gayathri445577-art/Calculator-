#Using a while loop, check whether a number
  #  is prerfect square.
    
a = int(input("enter the number"))
i = 1
while i*i <= a:
    if i*i == a:
        print("It is a perfect square")
        break
    i += 1
else:
    print("It is not a perfect square")
