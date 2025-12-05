length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width the rectangle: "))
length1 = int(input("Enter the length of the rectangle:"))
width1 = int(input("Enter the width of the rectangle: "))

area_of_rectangle1 = length1 * width1
area_of_rectangle2 = length * width

if area_of_rectangle1 > area_of_rectangle2:
    print("Area of rectangle 1 is greater")
elif area_of_rectangle1 < area_of_rectangle2:
    print("Area of rectangle 2 is greater")
else :
    print("both areas are equal")
