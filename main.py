path = "todos.txt"


def get_todo(filepath=path):
    """ Read a text file and return the content in a form of a list """

    with open(filepath, "r") as file:
        todos_file = file.readlines()
    return todos_file


def set_todo(data, filepath=path):
    """ Write a list in the text file """

    with open(filepath, "w") as file:
        file.writelines(data)


def get_user_answer():
    user_answer = input("Type add, show, edit, complete or exit:")
    return user_answer.strip()


complete_todos = []

while True:
    user_action = get_user_answer()

    if user_action.startswith("add"):
        todos = get_todo()
        todos.append(user_action[4:] + "\n")

        set_todo(todos)
    elif user_action.startswith("show"):
        todos = get_todo()
        for index, item in enumerate(todos):
            item = item.strip("\n").title()
            print(f"{index + 1}- {item}")

    elif user_action.startswith("edit"):
        try:
            num_todo = int(user_action[5:]) - 1

            todos = get_todo()
            try:
                item_to_edit = todos[num_todo].strip("\n")
                print(f"You will edit this item : {item_to_edit}")
                todos[num_todo] = input("Enter the new todo:") + "\n"
            except IndexError:
                print(f"There is no item with number {num_todo + 1}")
                continue

            set_todo(todos)

        except ValueError:
            print("Todo's number is not valid, please try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            num_todo = int(user_action[9:]) - 1

            todos = get_todo()
            todo_to_remove = todos[num_todo].strip("\n")
            complete_todos.append(todos[num_todo])
            del todos[num_todo]

            set_todo(todos)
            print(f"Todo '{todo_to_remove}' was removed from the list!")
        except IndexError:
            print(f"There is no item with number {num_todo + 1}")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print("***BYE***")





