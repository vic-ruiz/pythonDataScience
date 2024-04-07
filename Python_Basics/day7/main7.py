

while True:
    user_input = input("Type add, show, complete, edit or exit: ").strip().lower()
    match user_input:
        case "add":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            #todos = [i.strip("\n") for i in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index+1} - {item}")
        case "complete":
            number = int(input("Enter number of todo to complete: ")) - 1
            todo_completed = todos.pop(number)
            print(f"{todo_completed} was completed")
        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "exit":
            break

print("bye!")
