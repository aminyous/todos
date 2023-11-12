# print("Enter a todo")
#todos = []
complete_todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action == "add":
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(input("Enter a todo:") + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "show":
        with open("todos.txt", "r") as file:
            todos = file.readlines()


        #new_todos = []
        #for item in todos:
            # to remove the extra back slash (extra new line
            #new_todos.append(item.strip("\n"))

        # List comprehension - do the same as the above
        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            #item = item.strip("\n").title()
            print(f"{index + 1}- {item}")

    elif user_action == "edit":
        num_todo = int(input("type the number of todo to edit:")) - 1
        while num_todo <= len(todos) and num_todo >= 0:
            todos[num_todo] = input("Enter the new todo:")
            break

    elif user_action == "complete":
        print("Complete in progress")
        num_todo = int(input("type the number of todo to complete:"))
        complete_todos.append(todos[num_todo - 1])
        del todos[num_todo - 1]

    elif user_action == "exit":
        break

print("***BYE***")





