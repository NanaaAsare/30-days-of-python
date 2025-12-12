roman_numerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"

}

Number = int(input("Enter a number between 1 and 10: "))

if 1 <= Number <= 10:
    print(f"Roman numerals: {roman_numerals[Number]}")
else :
    print("Error , You have to enter number between 1 and 10")