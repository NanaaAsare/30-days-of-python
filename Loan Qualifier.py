min_salary = 30000
min_years_on_job = 2

salary = float(input("Enter your annual salary: "))
year_on_job = float(input("Enter the years on the Job: "))

if salary >= min_salary or  year_on_job >= min_years_on_job:
    print("Congratulations You qualify for the loan")
else:
    print("You do not qualify for the loan")