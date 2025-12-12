pocket = int(input("Enter a pocket number(0 -36): "))

if pocket < 0 or pocket > 36:
    print("Enter a number between 0 and 36.")
else:
    if pocket == 0:
        print("Green")
    elif 1 <= pocket <= 10:
        if pocket % 2 == 0:
            print("Black")
        else:
            print("red")
    elif 11 <= pocket <= 18:
        if pocket % 2 == 0:
            print("Red")
        else:
            print("Black")
    elif 19 <= pocket <= 28:
        if pocket % 2 == 0:
            print("Black")
        else:
            print("Red")
    elif 29 <= pocket <= 36:
        if pocket % 2 == 0:
            print("Red")
        else:
            print("Black")

