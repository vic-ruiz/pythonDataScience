from Python_Basics.day14.bonus.inches14 import inches_converter
from Python_Basics.day14.bonus.feets14 import feet_converter


def convert(feet, inches):
    feet = feet_converter(feet)
    inches = inches_converter(inches)
    meters = feet + inches
    return meters
