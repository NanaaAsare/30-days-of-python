A_score = 90
B_score = 80
C_score = 70
D_score = 60

grade = float(input("Enter your test score here: "))

if grade >= A_score:
    print("Excellent, You had an A ")
else:
    if  grade >= B_score:
        print("You had a B ")
    else:
        if grade >= C_score:
            print("You had a C")
        else:
            if grade >= D_score:
                print("You had a D ")
            else:
                print("You Failed!! ")