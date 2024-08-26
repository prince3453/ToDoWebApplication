from functions import file_write,file_read,print_todo

while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit : ").strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = file_read()
        todos.append(todo)
        file_write(todos)

    elif user_action.startswith("show"):
        todos = file_read()
        print_todo(todos)

    elif user_action.startswith("edit"):
        try:
            todos = file_read()
            number = int(user_action[5:])
            new_todo = input("Enter a new to-do : ") + "\n"
            todos[number-1] = new_todo
            file_write(todos)
        except ValueError:
            print("Your Command is not valid")
        except IndexError:
            print("Enter the valid number from the To-do items")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todos = file_read()
            todos_removed = todos[number].strip("\n")
            todos.pop(number)
            file_write(todos)

            message = f'Todo {todos_removed} removed from the list'
            print(message)
            print_todo(todos)
        except IndexError:
            print("Enter the valid number from the To-do items")
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid Input")

print("Bye!")