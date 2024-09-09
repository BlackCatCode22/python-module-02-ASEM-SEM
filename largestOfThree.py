def largest_Of_Three():
    x = int(input("Enter First number"))
    y = int(input("Enter Second number"))
    z = int(input("Enter Third number"))

    if x >= y and x>=z:
        print("largest number:", x)

    elif y >= x and y>=z:
        print("largest number:", y)

    else:
        print("largest number is :", z)

largest_Of_Three()

