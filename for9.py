#Find the sum of digits of a number using a for loop.
n = 768
sum = 0
for x in str(n):
    c=int(x)
    sum=sum+int(x)
print("Sum of digits:", sum)