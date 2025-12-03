def salary(hours_worked,hourly_rate,days_worked):
    gross_pay = hours_worked * hourly_rate * days_worked
    tax = gross_pay * 0.20
    net_salary = gross_pay - tax
    return net_salary


name = input("What your name: ")
hourly_rate = float(input("what's your hourly rate? "))
hours_worked = float(input("how many hours did you work? "))
days_worked = int(input("how days did you work in a month? "))

net_salary = salary(hours_worked, hourly_rate, days_worked)
print(f"{name}, Your monthly salary after 20% tax is : {net_salary}")