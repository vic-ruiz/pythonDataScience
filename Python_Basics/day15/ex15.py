import random

while True:
    try:
        lower_bound = int(input("Enter lower bound number: "))
        upper_bound = int(input("Enter upper bound number: "))
        random_numer = random.randint(lower_bound, upper_bound)
        print(random_numer)
        break
    except ValueError:
        print("Please enter a number")

