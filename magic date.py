Day = int(input("Enter a day: "))
Month = int(input("Enter a month: "))
Year = int(input("Enter a year: "))

magic_date = Month * Day == Year

if Month < 1 or Month > 12 :
    print("Error: Month must be between 1 to 12 ")
elif Day < 1 or Day > 31 :
    print("Error: Day must be between 1 to 31")
else:
    if magic_date == Year:
        print("The date is magic ")
    else:
        print("The date is not magic")