value = input("Enter any value: ")

print("You Entered: ", value)

if value.isdigit():
    print("Data type: Integer")

else:
    try:
        float(value)
        print("Data type: Float")
    except ValueError:
        print("Data type: String")