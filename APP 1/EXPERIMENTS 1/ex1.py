todos = []

while True:
    user_action = input("type add, show or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo =input("TODO:   ")
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case whatever:
            print("WHAT THE FUCK IS WRONG WITH YOU???? CHOSE ONE OF ABOVE BITCH")
print("BYE BYE")