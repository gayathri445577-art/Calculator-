#To convert a number into binary number
a = int(input("ente the number"))
binary = ""
while a > 0:
    r = a % 2
    binary = str(r) + binary
    a = a // 2
print("Binary number is", binary)