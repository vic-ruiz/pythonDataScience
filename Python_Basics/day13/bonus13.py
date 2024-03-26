def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    parts = [float(i) for i in parts]
    feet = parts[0]
    inches = parts[1]
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    feet = feet_converter(feet)
    inches = inches_converter(inches)
    meters = feet + inches
    return meters


def feet_converter(feet):
    feet = feet * 0.3048
    return feet


def inches_converter(inches):
    inches = inches * 0.0254
    return inches


feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

total = convert(parsed["feet"], parsed["inches"])
print(total)


