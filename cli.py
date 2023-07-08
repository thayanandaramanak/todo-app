# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d %Y, %H:%M:%S")
print("it iS", now)
while True:
    user_action= input("enter add,show ,edit,complete or exit:")
    user_action=user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos=functions.get_todos()

        todos.append(todo+'\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos=functions.get_todos()


        for count,items in enumerate(todos):
            items=items.strip('\n')
            row=f"{count+1}-{items}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number= int(user_action[5:])
            number=number-1

            todos=functions.get_todos()

            new_todo=input("enter the input:")
            todos[number]=new_todo +'\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number= int(user_action[9:])

            todos=functions.get_todos()

            index=number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message=f"todo {todo_to_remove} was remove from the list"
            print(message)
        except IndexError:
            print("There is no item in this number.")
            continue

    elif user_action.startswith('exit') :
        break
    else:
        print('invalid command')
print("Bye!")
