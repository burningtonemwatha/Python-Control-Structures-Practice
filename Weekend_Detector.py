day = int(input("Enter a number (1-7) representing the day of the week: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 | 6 | 7:
        print("looking forward to the weekend!")

    case _:
        print("Invalid day number! Please enter a number between 1 and 7.")
    