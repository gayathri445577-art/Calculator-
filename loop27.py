a = int(input("Enter number: "))
l = s = -1
while a > 0:
    d = a % 10
    if d > l:
        s = l
        l = d
    elif d > s and d != l:
        s = d
    a //= 10

print("Second largest digit:", s)