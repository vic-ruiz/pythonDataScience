todos = []

while True:
    user_input = input("Type add, show, complete, edit or exit: ").strip().lower()
    match user_input:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
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
