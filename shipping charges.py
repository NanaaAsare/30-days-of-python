#ask the user of the weight of the package

weight_of_package = float(input("Enter the weight of the car: "))

if weight_of_package <= 2:
    rate = 1.50
elif weight_of_package <= 6:
    rate = 3.00
elif weight_of_package <= 10:
    rate = 4.00
else:
    rate = 4.75

#calculating shipping charges
shipping_charges = weight_of_package * rate

#Displaynig the result
print(f"Your weight is {weight_of_package:.2f}")
print(f"Your shipping charge is {shipping_charges:.2f}")