numbers = [20, 30, 49, 87, 10, 20, 90, 80, 20]
duplicate = []
for number in numbers:
    if number not in duplicate:
        duplicate.append(number)
print(duplicate)