from modules.functions import *
import time


complete_todos = []


while True:
    now = time.strftime("%d-%b-%Y, %H:%M:%S")

    print(f"It is : {now}")
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

            item_to_edit = todos[num_todo].strip("\n")
            print(f"You will edit this item : {item_to_edit}")
            todos[num_todo] = input("Enter the new todo:") + "\n"

            set_todo(todos)

        except ValueError:
            print(f"Todo's number is not valid : {user_action[5:]}, please try again.")
            continue
        except IndexError:
            print(f"There is no item with number : {num_todo + 1}")
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

    print("\n")

print("***BYE***")





