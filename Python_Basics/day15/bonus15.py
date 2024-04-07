import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)
counter = 0

for question in data:
    print(question["question"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


for index, question in enumerate(data):
    message = f"Question-{index + 1} : Your answer was {question['user_choice']} ." \
              f" Correct answer was {question['correct_answer']}"
    if question["user_choice"] == question["correct_answer"]:
        counter = counter + 1
        print(message)
        print("Correct Answer")
    else:
        print(message)
        print("Wrong Answer")


print(f"Correct answers {counter}/{len(data)}")
