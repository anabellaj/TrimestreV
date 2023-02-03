datasets = [
    { "Nombre": "Common Crawl", "Cantidad de tokens": 410000000000, "Tokens para set de entrenamiento (%)": 60 },
    { "Nombre": "WebText2", "Cantidad de tokens": 19000000000, "Tokens para set de entrenamiento (%)": 22 },
    { "Nombre": "Books 1", "Cantidad de tokens": 12000000000, "Tokens para set de entrenamiento (%)": 8 },
    { "Nombre": "Books 2", "Cantidad de tokens": 55000000000, "Tokens para set de entrenamiento (%)": 8 },
    { "Nombre": "Wikipedia", "Cantidad de tokens": 3000000000, "Tokens para set de entrenamiento (%)": 3 },
]
while True:
    print ('\t----BIENVENIDO----\nAca puede obtener informacion sobre tus datasets.')
    opt = input ('\nQue deseas realizar hoy?\n1. Consultar todos los datasets\n2. Modificar porcentajes\n3. Mostrar estadisticas\n4. Salir\nIngresa la opcion que desees llevar a cabo\n>>> ')
    # Validar input
    while opt not in ['1','2','3','4']:
        opt = input ('\nERROR\nPor favor ingresa una opcion valida!\nQue deseas realizar hoy?\n1. Consultar todos los datasets\n2. Modificar porcentajes\n3. Mostrar estadisticas\n4. Salir\nIngresa la opcion que desees llevar a cabo\n>>> ')
    # Opcion 1: Mostrar todos los datasets
    if opt == '1':
        for dataset in datasets:
            print(f"----------{dataset['Nombre']}-----------\nCantidad de tokens: {dataset['Cantidad de tokens']}\nPorcentaje de tokens para set de entrenamiento: {dataset['Tokens para set de entrenamiento (%)']}")
            tokens_totales = (dataset["Tokens para set de entrenamiento (%)"]/100) * dataset["Cantidad de tokens"]
            print (f'Cantidad de tokens para set de entranmiento: {tokens_totales}\n')
    # Opcion 2: Modificar el porcentaje de algun dataset
    elif opt == '2':
        while True:
            modify = input('\nIngresa el nombre del dataset a modificar (incluye las mayusculas!):\n>>> ')
            keep = 0
            go = ''
            for dataset in datasets:
                compare = dataset.get('Nombre')
                if modify == compare:
                        while True:
                            try:
                                porcentaje = int(input('\nIngresa el porcentaje nuevo para el dataset elegido\nRecuerda que debe ser un numero entre 3 y 74:\n>>> '))
                                if porcentaje > 74 or porcentaje <3:
                                    continue
                                else:
                                    break
                            except:
                                print ('\nRecuerda ingresar un numero!')
                                continue
                        dataset["Tokens para set de entrenamiento (%)"] = porcentaje
                        keep += 1
                        break
            if keep == 0:
                go = input ('\nDatabase no encontrado\nIngresa "S" para seguir o cualquier tecla para volver al menu principal:\n>>> ')
                if go == 'S':
                    continue
                else:
                    break
    # Opcion 3: Mostrar estadisticas
    elif opt == '3':    
        # Total de tokens entre todos # Dataset con menor y mayor porcentaje
        total = 0
        porcentajes = []
        for dataset in datasets:
            total += dataset["Cantidad de tokens"]
            add = dataset["Tokens para set de entrenamiento (%)"]
            porcentajes.append(add)
        porcentajes.sort()
        print (f'\nTotal de tokens entre todos los database: {total}\nDatabase con el menor porcentaje de tokens para set de entrenamiento: {porcentajes[0]}')
        porcentajes.reverse()
        print (f'Database con el mayor porcentaje de tokens para set de entrenamiento: {porcentajes[0]}\n')
    # Opcion #4: Salir
    elif opt == '4':
        print ('\nHasta pronto!')
        break


        
