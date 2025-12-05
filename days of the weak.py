

Days_of_the_week = int(input("Enter a number from 1 through 7: "))

if Days_of_the_week >= 1 and Days_of_the_week <= 7:

        if Days_of_the_week == 1:
            print("It's Monday")
        elif Days_of_the_week == 2:
            print("It's Tuesday")
        elif Days_of_the_week == 3:
            print("It's Wednesday")
        elif Days_of_the_week == 4:
            print("It's Thursday")
        elif Days_of_the_week == 5:
            print("It's Friday")
        elif Days_of_the_week == 6:
            print("It's Saturday")
        else:
            print("It's Sunday")
else:
    print("Please Enter a number from 1 to 7")


