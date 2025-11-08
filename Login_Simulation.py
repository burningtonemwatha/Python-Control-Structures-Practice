stored_email = "user@example.com"
stored_password = "12345"

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == stored_email and password == stored_password:
    print("Login Successful!")

else:
    print("Invalid Credentials!")
