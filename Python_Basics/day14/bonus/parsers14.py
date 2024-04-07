def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    parts = [float(i) for i in parts]
    feet = parts[0]
    inches = parts[1]
    return {"feet": feet, "inches": inches}
