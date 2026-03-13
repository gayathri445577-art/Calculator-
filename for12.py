#reverse a string
s = input("enter the string")
rev = " "
for i in range(len(s)-1, -1, -1):
    rev = rev + s[i]
print("Reversed string:", rev)