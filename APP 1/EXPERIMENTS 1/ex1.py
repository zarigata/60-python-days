todos = []

while True:
    user_action = input("type add, show, edit or exit:")
    user_action = user_action.strip()
    match user_action:
        #ADD
        case 'add':
            todo =input("TODO:   ")
            todos.append(todo)
        #SHOW
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        #EDITOR OF TASKS
        case 'edit':
            number = int(input("Number of the todo to edit"))
            number = number - 1
            new_todos =input("Imput the new todo")
            todos[number] = new_todos
        #LEAVE
        case 'exit' | 'leave' | 'quit' | 'close':
            break
        #EVERITHNG ELSE
        case whatever:
            print("WHAT THE FUCK IS WRONG WITH YOU???? CHOSE ONE OF ABOVE BITCH")

print("BYE BYE")