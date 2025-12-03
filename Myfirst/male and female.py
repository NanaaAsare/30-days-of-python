Number_of_students = float(input("How many students are in the class: "))
Number_of_males = float(input("how many of them are males: "))
Number_of_females = float(input("How many are females: "))

percentage_of_males = Number_of_males/Number_of_students * 100
percentage_of_females = Number_of_females/Number_of_students * 100

print(f"the percentage of male students are: {percentage_of_males:.2f} %")
print(f"the percentage of female students are: {percentage_of_females:.2f} %")