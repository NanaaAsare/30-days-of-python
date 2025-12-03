percent_tip = 0.18
sales_tax = 0.07

charge_for_food = float(input("Enter the charge for food: "))

tip_tax = charge_for_food * percent_tip
tax_sales = charge_for_food * sales_tax
total_tax = tip_tax + tax_sales
total = total_tax + charge_for_food

print(f"your tip tax for the food is ${tip_tax}")
print(f"your tax sale for the food is ${tax_sales:.2f}")
print(f"your total tax sale for the food is ${total_tax}")
print(f"your total amount payable after tax is ${total}")