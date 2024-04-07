datetime = input("Enter today's date: ")
mood = input("How do you rate yout mood today from 1 to 10?: ")
comments = input("Let your thoughts flow: ")
path = f"journal/{datetime}.txt"

with open(path, "w") as file:
    file.write(mood+"\n")
    file.write(comments)
with open(path, "r") as file:
    content = file.readlines()

print(content)