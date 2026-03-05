#check the list of numbers greate than 10
a = [1, 2, 3, 4, 7,20,45,100,15]
count = 0
index = 0
while index < len(a): 
    if a[index] <10:
        count += 1
    index += 1
print("the count is",count) 