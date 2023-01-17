# Crear un diccionario en donde la clave es la cedula y el valor otro diccionario con los datos
# (nombre, direccion, correo, preferente[True or False])
# Opciones 1. Crear cliente 2. Eliminar 3. Mostrar 4. Listar todos 5. Listar preferentes 6. Salir 

clientes = {}
options = ['1','2','3','4','5','6']
run = ''
print ('\nBienvenido a su Base de Datos!\nQue desea hacer hoy?')
while run != 6:
    print ('\nPuede elegir entre:\n1. Crear cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos los clientes\n5. Listar clientes preferenciales\n6. Salir')
    run = input('\nElija una opcion ingresando el numero correspondiente: ')
    while run not in options or not run.isnumeric():
        print ('Opcion invalida')
        print ('\nPuede elegir entre:\n1. Crear cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos los clientes\n5. Listar clientes preferenciales\n6. Salir')
        run = input('\nElija una opcion ingresando el numero correspondiente: ')
    run = int(run)

    #Agregar cliente
    if run == 1:
        cedula = input('\nIngrese la cedula del cliente:\n>')
        nombre = input('\nIngrese el nombre completo del cliente:\n>')
        direccion = input('\nIngrese la direccion del cliente:\n>')
        correo = input('\nIngrese el correo del cliente:\n>')
        preferente = input('\nEs un cliente preferente? Coloque si o no\n>').title()
        while preferente != 'Si' and preferente != 'No':
            print ('Ingreso invalido')
            preferente = input('\nEs un cliente preferente? Coloque si o no\n>').title()
        cliente = {'Nombre': nombre, 'Direccion': direccion, 'Correo': correo, 'Preferente': preferente=='Si'}
        clientes[cedula] = cliente

    #Eliminar cliente
    if run == 2:
        cedula = input('\nIngrese la cedula del cliente que desea eliminar:\n>')
        if cedula in clientes:
            del clientes[cedula]
        else:
            print(f'\nNo existe cliente con la cedula {cedula}.')

    #Mostrar cliente especifico
    if run == 3:
        cedula = input('\nIngrese la cedula del cliente para acceder a sus datos:\n>')
        if cedula in clientes:  
            for k, v in clientes.items():
                if k == cedula:
                    print (k, v)
        else:
            print(f'\nNo existe cliente con la cedula {cedula}.')
    
    #Mostrar todos los clientes (solo nombres)
    if run == 4:
        print ('\nLista de clientes:')
        for key, nombre in clientes.items():
            nombres = nombre.get('Nombre')
            print(key, nombres)
    
    #Mostrar clientes preferenciales:
    if run == 5:
        print ('\nClientes preferenciales:')
        for k, v in clientes.items():
            vip = v.get('Preferente')
            if vip == True:
                print (k, v['Nombre'])


    if run == 6:
        print ('\nHasta pronto!\n')