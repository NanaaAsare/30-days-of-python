state_tax = 0.05
county_tax = 0.025
purchase = int(input("Enter the amount of purchase: "))

purchase_after_state_tax = state_tax * purchase
purchase_after_county_tax = county_tax * purchase
total_tax = purchase_after_county_tax + purchase_after_state_tax

total_sale = purchase + total_tax
print(purchase)
print(purchase_after_state_tax)
print(purchase_after_county_tax)
print(total_tax)
print(total_sale)


