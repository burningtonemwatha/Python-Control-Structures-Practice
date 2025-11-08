age = int(input("Enter your age: "))

if age > 18:
    print("Access granted - You receive a complimentary drink!")
elif 16 <= age <= 18:
    print("Access granted - Enjoy a juice pack!")
else: 
    print("Access denied - You're too young to enter!")    