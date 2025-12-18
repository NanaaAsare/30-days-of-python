# constant price per package
price_package = 99

# asking the user the number of packages purchased

package_purchased = int(input("Enter the number of packages purchased: "))

# Discount rate based on quantity
if package_purchased >= 10:
    discount_rate = 0.10
elif package_purchased >=20:
    discount_rate = 0.20
elif package_purchased >= 50:
    discount_rate = 0.30
elif package_purchased >= 100:
    discount_rate = 0.40
else:
    discount_rate = 0.00

#calculating the full item price
full_price = price_package * package_purchased
discount_amount = full_price * discount_rate
total_amount = full_price - discount_amount

# printing the output
print(f"discount amount: ${discount_amount:.2f}")
print(f"total amount: ${total_amount:.2f}")