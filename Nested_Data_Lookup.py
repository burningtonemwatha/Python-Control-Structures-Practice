myFamily = {
    "father": { "name": "John", "year": 1985 },
    "mother": { "name": "Jane", "year": 1990 },
}

member = input("Enter family member (father/mother): ").lower()

if member in myFamily:
    print("Name: ", myFamily[member]["name"])
    print("Birth Year: ", myFamily[member]["year"])

else:
    print("Family Member Not Found.")