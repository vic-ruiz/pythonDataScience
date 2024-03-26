def get_todos():
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_input = input("Type add, show, complete, edit or exit: ")

    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            todos = file.writelines(todos)

    elif user_input.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1} - {item}")

    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:]) - 1

            todos = get_todos()

            todo_completed = todos.pop(number).strip("\n")
            print(f"{todo_completed} was completed")

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:]) - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("bye!")
