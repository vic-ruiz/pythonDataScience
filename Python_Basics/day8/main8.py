

while True:
    user_input = input("Type add, show, complete, edit or exit: ").strip().lower()
    match user_input:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1} - {item}")

        case "complete":
            number = int(input("Enter number of todo to complete: ")) - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todo_completed = todos.pop(number).strip("\n")
            print(f"{todo_completed} was completed")

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break

print("bye!")
