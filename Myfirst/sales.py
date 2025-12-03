Tax = 0.7
cart1 = float(input("enter price of first item: "))
cart2= float(input("enter price of second item: "))
cart3 = float(input("enter price of third item: "))
cart4 = float(input("enter price of fourth item: "))
cart5 = float(input("enter price of firth item: "))

total_price = cart1 + cart2 + cart3 + cart4 + cart5
amount_with_tax = total_price * Tax

print(f"the total price after tax {amount_with_tax:.2f} ")