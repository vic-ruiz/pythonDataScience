while True:
    user_input = input("Type add, show, complete, edit or exit: ")

    if "add" in user_input:
        todo = user_input[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            todos = file.writelines(todos)

    elif "show" in user_input:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1} - {item}")

    elif "complete" in user_input:
        number = int(user_input[9:]) - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo_completed = todos.pop(number).strip("\n")
        print(f"{todo_completed} was completed")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "edit" in user_input:
        number = int(user_input[5:]) - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "exit" in user_input:
        break
    else:
        print("Command is not valid")

print("bye!")
