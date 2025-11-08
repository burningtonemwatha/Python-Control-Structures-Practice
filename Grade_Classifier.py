score = int(input("Enter your test score (0-100): "))

if 80 <= score <= 100:
    print("Excellent!")
elif 50 <= score <= 79:
    print("Good!")
elif 0 <= score <= 49:
    print("Needs Improvement!")
else:
    print("Invalid score. Please enter a score between 0 and 100.")