# Asking the user for height and weight
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

#Calculating  BMI
BMI = (weight * 703) / (height ** 2)

#Deteminining if the person is overweight,underweight or has optimal weight
if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You have a normal weight")
elif BMI < 30:
    print("you are overweight")
else :
    print("You are Obese")

#Displaying  result
print(f"Your BMI is {BMI:.2f}")