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


if __name__ == "__main__":
    print(__name__)

