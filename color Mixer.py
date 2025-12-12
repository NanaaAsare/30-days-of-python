# Primary color
Primary_color = {"red","yellow","blue"}

color1 = input("Enter the first primary color: ").strip().lower()
color2 = input("Enter the second primary color: ").strip().lower()


if color1 not in  Primary_color or color2 not in Primary_color:
    print("one or both are not primary colors")
elif color1 == color2:
    print("Please enter two different primary colors")
# determine the secondary color
else:
    if {"red", "blue"} == {color1, color2}:
        print("The secondary color is PURPLE")
    elif {"red" , "yellow"} == {color1, color2}:
        print("The secondary color is ORANGE")
    elif {"blue" , "yellow"} == {color1 , color2}:
        print("The secondary color is GREEN")
