#login sysyem
username = input("Enter username: ")
password = input("Enter password: ")
if username == "gayathri" and password == "1234":
    print("Login successful")
elif username != "gayathri":
    print("Incorrect username")
elif password != "1234":
    print("Incorrect password")
else:
    print("Login failed")