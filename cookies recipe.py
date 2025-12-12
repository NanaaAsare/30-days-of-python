sugar = 1.5
butter = 1
flour = 2.75
done_recipe = 48

cookie_wanted = int(input("Enter how many cookies you want: "))

factor = cookie_wanted / done_recipe

required_sugar = sugar / factor
required_butter = butter / factor
required_flour = flour / factor

print(f"Ingredients needed")
print(f"Sugar: {required_sugar:.2f} cups")
print(f"butter: {required_butter:2f} cups")
print(f"flour: {required_flour:.2f} cups")
