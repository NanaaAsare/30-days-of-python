weigth = int(input("how much do you weigh: "))
unit = input("(L)bs or (K)g? ")
if unit.upper() == "L":
    converted_kg = weigth * 0.453
    print(f"You are {converted_kg}  kilos")
else :
    converted_lbs =weigth / 0.453
    print(f"You are {converted_lbs} lbs")

