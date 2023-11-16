# print("Enter a todo")
#todos = []
complete_todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if "add" in user_action:
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # todos.append(input("Enter a todo:") + "\n")
        todos.append(user_action[4:] + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n").title()
            print(f"{index + 1}- {item}")

    elif "edit" in user_action:
        num_todo = int(input("type the number of todo to edit:")) - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        while num_todo <= len(todos) and num_todo >= 0:
            todos[num_todo] = input("Enter the new todo:") + "\n"
            break

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        print("Complete in progress")
        num_todo = int(input("type the number of todo to complete:"))

        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todo_to_remove = todos[num_todo - 1].strip("\n")
        complete_todos.append(todos[num_todo - 1])
        del todos[num_todo - 1]

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print(f"Todo {todo_to_remove} was removed from the list!")

    elif "exit" in user_action:
        break

print("***BYE***")





