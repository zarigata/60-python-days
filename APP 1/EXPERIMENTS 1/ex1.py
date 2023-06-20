todos = []

while True:
    user_action = input("Mostrar itens a fazer ou adicionar um novo?")
    match user_action:
        case 'add':
            todo =input("a fazer")
            todos.append(todo)
        case 'show':
            print (todo)

