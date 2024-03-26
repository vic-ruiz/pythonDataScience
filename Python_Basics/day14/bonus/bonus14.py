from Python_Basics.day14.bonus.converters14 import convert
from Python_Basics.day14.bonus.parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

total = convert(parsed["feet"], parsed["inches"])
print(total)


