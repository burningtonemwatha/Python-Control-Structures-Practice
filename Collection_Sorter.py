numbers = [3, 78, 12, 2, 8, 9, 100, 66, 5, 11, 23, 29, 19, 10, 18, 55, 70, 42, 37, 90]
count = 0

for num in numbers:
    if num <= 10:
        continue
    print(num)
    count += 1

print("Total numbers greater than 10: ", count)