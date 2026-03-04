#check the number  is armstrong or not
a = int(input("Enter the number: "))
temp = a
count = 0
while temp > 0:
    count += 1
    temp = temp // 10
temp = a
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10
if total == a:
    print("Armstrong")
else:
    print("Not Armstrong")