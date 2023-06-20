todos = []

while True:
    user_action = input("type add, show or exit:")
    match user_action:
        case 'add':
            todo =input("TODO:   ")
            todos.append(todo)

        case 'show':
            print (todos)
        case 'exit':
            break
print("BYE BYE")