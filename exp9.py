#check whethwr a number is
#perfect square
#perfect cube
#both 
  
import math
num = int(input("Enter a number: "))
a = math.sqrt(num)
root = round(num ** (1/3))  
if a == int(a) and root**3 == num:  
    print("Perfect Square and Perfect Cube")
elif a == int(a):
    print("Perfect Square")
elif root**3 == num:  
    print("Perfect Cube")
else:
    print("Not a Perfect Square or Cube")