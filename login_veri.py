# Login Verification System

username = input("Enter username: ").lower()
password = input("Enter password: ").lower()

if username == "admin" and password == "1234":
    print("Login Successful")

else:
    print("Invalid username or password")