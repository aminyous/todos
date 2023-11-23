complete_todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(user_action[4:] + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n").title()
            print(f"{index + 1}- {item}")

    elif user_action.startswith("edit"):
        try:
            num_todo = int(user_action[5:]) - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            try:
                item_to_edit = todos[num_todo].strip("\n")
                print(f"You will edit this item : {item_to_edit}")
                todos[num_todo] = input("Enter the new todo:") + "\n"
            except IndexError:
                print(f"There is no item with number {num_todo + 1}")
                continue

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Todo's number is not valid, please try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            num_todo = int(user_action[9:]) - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todo_to_remove = todos[num_todo].strip("\n")
            complete_todos.append(todos[num_todo])
            del todos[num_todo]

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print(f"Todo '{todo_to_remove}' was removed from the list!")
        except IndexError:
            print(f"There is no item with number {num_todo + 1}")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print("***BYE***")





