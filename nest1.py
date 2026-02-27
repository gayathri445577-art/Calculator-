# ≥ 50 → Second Class
# Else → Just Pass
# Else → Fail
a=int(input("enter the number"))
if a >= 35:
    print("pass")
    if a >= 75:
        print("distinction")
    elif a >= 60:
        print("first class")
    elif a >= 50:
        print("second class")
    else:
        print("just pass")
else:
    print("fail")