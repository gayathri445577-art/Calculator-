#check the list of numbers greate than 10
a = [1, 2, 3, 4, 7,20,45,100,15]
count_greater= 0
count_less=0
index = 0
while index < len(a): 
    if a[index] >10:
    	count_greater += 1
    elif a[index]<10:
        count_less+=1
    index += 1
print("count_greater is",count_greater)
print("count_less is",count_less)