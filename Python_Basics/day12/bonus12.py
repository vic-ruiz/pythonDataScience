def convert(feet_inches_arg):
    parts = split_list(feet_inches_arg)
    feet = parts[0]
    inches = parts[1]
    feet = feet_converter(feet)
    inches = inches_converter(inches)
    total_local = feet + inches
    return total_local


def split_list(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    parts = [float(i) for i in parts]
    return parts


def feet_converter(feet):
    feet = feet * 0.3048
    return feet


def inches_converter(inches):
    inches = inches * 0.0254
    return inches


feet_inches = input("Enter feet and inches: ")

total = convert(feet_inches)
print(total)
