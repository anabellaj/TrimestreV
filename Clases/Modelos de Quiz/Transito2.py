infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678}
}

infractors = {}

count = 0
print ('\nWelcome to the transport department!')
while True:
    try:
        option = int(input('What do you wish to do today?\n1. Add infractor to database\n2. Remove infractor from database\n3. Show registered fines\n4. Exit\n\nEnter the number corresponding to the option of your choice:\n>>'))
        if option not in [1,2,3,4]:
            continue
        else:
            pass
    except:
        print ('\nOops! Seems like you entered an invalid option. Please try again.')
        continue
    # Option 1: Add infractor (name, surname, id, type, officer)
    if option == 1:
        count += 1
        name = input('\nPlease enter the name of the infractor:\n>>')
        lastName = input('\nPlease enter the last name of the infractor:\n>>')
        while True:
            try:
                id = int(input('\nPlease enter the id of the infractor:\n>>'))
                break
            except:
                print ('Please enter only numbers.')
                continue
        while True:
            try:
                officer = int(input('\nPlease enter the number of the officer in charge just like it appears on the screen:\n1. Luis Bello\n2. Antonio Guerra\n3. Jose Quevedo\n>>'))
                if int(officer) not in [1,2,3]:
                    continue
                else:
                    break
            except:
                print ('Please enter a valid option.')
                continue            
        if officer == 1:
            off = officers[1]
        elif officer == 2:
            off = officers[3]
        elif officer == 3:
            off = officers[2]
        infractors.update({count: {'name':name, 'lastName': lastName, 'id': id, 'officer': off}})
        print (infractors)
    # Option 2: Remove infractor from database
    # elif option == 2:

    # Option 3: Show registered fines

    # Option 4: Exit
    elif option == 4:
        print ('Goodbye!')
        break