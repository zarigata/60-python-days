todos = []

while True:
    user_action = input("type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        #ADD
        case 'add':
            todo =input("TODO:   ")
            todos.append(todo)
        #SHOW
        case 'show' | 'display':
            for index, item in enumerate(todos):
                index = index + 1
                item = item.title()
                print(index,'--', item)
        #EDITOR OF TASKS
        case 'edit':
            number = int(input("Number of the todo to edit"))
            number = number - 1
            new_todos =input("Imput the new todo")
            todos[number] = new_todos
        #COMPLETADOR
        case 'complete':
            number = int(input("Number of the todo to complete"))
            todos.pop(number - 1)
        #LEAVE
        case 'exit' | 'leave' | 'quit' | 'close':
            break
        #EVERITHNG ELSE
        case whatever:
            print("WHAT THE FUCK IS WRONG WITH YOU???? CHOSE ONE OF ABOVE BITCH")

print("BYE BYE")