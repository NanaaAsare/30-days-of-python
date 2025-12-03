name = input("What is your name? ")

if len(name) < 3:
    print("name must be atleast 3 characters")
elif len(name) > 50:
    print("name must be maximum of 50 characters")
else:
    print("name looks good")