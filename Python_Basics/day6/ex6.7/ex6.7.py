for item in "abc":
    path = f"{item}.txt"
    file = open(path, "r")
    text = file.read()
    file.close()
    print(text)