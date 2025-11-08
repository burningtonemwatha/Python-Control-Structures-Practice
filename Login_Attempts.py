password = "pass123"
attempts = 0

while attempts < 3:
    user_input = input("Enter your password: ")
    if user_input == password:
        print("Access Granted")
        break
    else:
        print("Wrong Password, Try Again.")
        attempts += 1

if attempts == 3:
    print("Account Locked!")