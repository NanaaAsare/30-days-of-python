
# Asking the user to enter number of seconds.
Number_of_seconds = int(input("Enter the number of seconds: "))

if Number_of_seconds >=86400:
    minutes = Number_of_seconds / 86400
    print(f"{Number_of_seconds} seconds is equal to {minutes:.2f} minutes")
elif Number_of_seconds >= 3600:
    hours  = Number_of_seconds / 3600
    print(f"{Number_of_seconds} hours is equal to {hours:.2f} hours")
elif Number_of_seconds >= 60:
    days = Number_of_seconds / 60
    print(f"{Number_of_seconds} days is equal to {days:.2f} days")
else:
    print(f"{Number_of_seconds} seconds is less than a minute")