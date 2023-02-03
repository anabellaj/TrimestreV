miau_edd = [
    {
        'name':'Pelusa',
        'gender': 'Male',
        'age': 9,
        'weight': 3.5,
        'colour':'Blanco',
        'vaccinated': False
    },
    {
        'name':'Oreo',
        'gender': 'Female',
        'age': 1,
        'weight': 3.7,
        'colour':'Blanco y Negro',
        'vaccinated': False
    },
    {
        'name':'Bebeso',
        'gender': 'Female',
        'age': 10,
        'weight': 4.1,
        'colour':'Blanco',
        'vaccinated': False
    },
    {
        'name':'Lilly',
        'gender': 'Female',
        'age': 2,
        'weight': 4.5,
        'colour':'Naranja',
        'vaccinated': False
    }
]
while True:
    opt = input('\nBienvenido a Arca Unimet! Que desea realizar hoy?\n1. Consultar todos los gatos\n2. Ver las estadisticas\n3. Hacer chequeo medico a los gatos\n4. Salir\n>>> ')
    while opt not in ['1','2','3','4']:
        opt = input ('\nPor favor ingrese una opcion valida:\n1. Consultar todos los gatos\n2. Ver las estadisticas\n3. Hacer chequeo medico a los gatos\n4. Salir\n>>> ')
    
    # Opcion 1: Imprimir todos los datos 
    if opt == '1':
        print ('\t\tGATOS DISPONIBLES')
        for gatos in miau_edd:
            for key, value in gatos.items():
                if key == 'name':
                    print ('------------------',gatos['name'],'------------------')
                if key == 'gender':
                    print ('Gender:',gatos['gender'])
                if key == 'age':
                    print ('Age:',gatos['age'],'years')
                if key == 'weight':
                    print ('Weight:', gatos['weight'],'kg')
                if key == 'colour':
                    print ('Color:', gatos['colour'])
                if key == 'vaccinated':
                    if gatos[key] == True:
                        print ('Vaccinated: Yes\n')
                    if gatos [key] == False:
                        print ('Vaccinated: No\n')
    # Option 2: Mostrar estadisticas
    elif opt == '2':
        # N de gatos vacunados. gato mas gordo y mas flaco, nombre mas largo, promedio de edad y peso
        vaccinated_count = 0
        pesos = []
        for gatos in miau_edd:
            if gatos['vaccinated'] == True:
                vaccinated_count += 1
            pesos.append(gatos['weight'])
            
            

