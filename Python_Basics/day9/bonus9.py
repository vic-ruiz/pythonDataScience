while True:
    password = input("Enter password: ")
    check_len = False
    check_digits = False
    check_upper = False

    conditions = {}

    if len(password) >= 8:
        check_len = True

    conditions["length"] = check_len

    for item in password:
        if item.isupper():
            check_upper = True

    conditions["upper"] = check_upper

    for item in password:
        if item.isdigit():
            check_digits = True

    conditions["digit"] = check_digits

    if all(conditions.values()):
        print("Strong Password")
        break
    else:
        print("Weak sauce")
