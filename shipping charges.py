#ask the user of the weight of the package

weight_of_package = int(input("Enter the weight of the car: "))

if weight_of_package <= 2:
    print("your charge is $ 1.50")
elif 2 > weight_of_package < 6:
    print("your charge is $ 3.00")
elif 6 > weight_of_package < 10:
    print("Your charge is $ 4.00")
elif weight_of_package > 10:
    print("Your charge is $ 4.75")

print(f"Your weight is {weight_of_package:.2f}")