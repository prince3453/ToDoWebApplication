def file_write(todos):
    with open("todos.txt", "w") as file:
        file.writelines(todos)

def file_read():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos

def print_todo(todos):
    for index, item in enumerate(todos):
        print(index + 1, ":", item, end="")