purchased_books = int(input("Enter the number of purchased books: "))

if purchased_books == 0:
    print("You have earned zero points")
elif purchased_books == 2:
    print("You have earned 5 points")
elif purchased_books == 4 :
    print("You have earned 15 points")
elif purchased_books == 6:
    print("You had earned 30 points ")
elif purchased_books >= 8:
    print("you have earned 60 points")
