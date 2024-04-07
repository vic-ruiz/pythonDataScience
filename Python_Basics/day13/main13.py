def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write to-do items list in text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


while True:
    user_input = input("Type add, show, complete, edit or exit: ")

    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_input.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1} - {item}")

    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:]) - 1

            todos = get_todos()

            todo_completed = todos.pop(number).strip("\n")
            print(f"{todo_completed} was completed")

            write_todos(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:]) - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("bye!")
