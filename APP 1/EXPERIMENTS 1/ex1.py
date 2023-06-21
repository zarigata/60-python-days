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

        case 'edit':
            print ("10-4")
        #LEAVE
        case 'exit' | 'leave' | 'quit' | 'close':
            break
        #EVERITHNG ELSE
        case whatever:
            print("WHAT THE FUCK IS WRONG WITH YOU???? CHOSE ONE OF ABOVE BITCH")

print("BYE BYE")