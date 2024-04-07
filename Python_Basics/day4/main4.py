todos = []

while True:
    user_input = input("Type add, show, edit or exit: ").strip().lower()
    match user_input:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item.capitalize())

        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "exit":
            break

print("bye!")
