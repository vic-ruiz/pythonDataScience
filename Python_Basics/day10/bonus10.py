try:
    width = float(input("Enter the rectangle width: "))
    length = float(input("Enter the rectangle length: "))
    if width != length:
        area = width * length
        print(area)
    else:
        exit("That's a square")
except ValueError:
    print("Please enter a number")


