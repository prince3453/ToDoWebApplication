FILEPATH = "todos.txt"

def file_write(todos, filepath = FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)

def file_read(filepath = FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def print_todo(todos):
    for index, item in enumerate(todos):
        print(index + 1, ":", item, end="")