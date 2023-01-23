anime = {
"Demon Slayer": {
"Temporada 1": [
{
"cap": 1,
"name": "Crueldad",
"duration": "23:39"
},
{
"cap": 4,
"name": "Selección final",
"duration": "23:40"
},
{
"cap": 19,
"name": "Dios del fuego",
"duration": "23:40"
},
{
"cap": 26,
"name": "Una nueva misión",
"duration": "24:10"
}
],
"Temporada 2": [
{
"cap": 35,
"name": "Un sueño profundo",
"duration": "22:55"
},
{
"cap": 43,
"name": "¡No me rendiré!",
"duration": "23:40"
}
]
},
"Spy x Family": {
"Temporada 1":[
{
"cap": 4,
"name": "Objetivo: pasar la entrevista",
"duration": "24:10"
},
{
"cap": 7,
"name": "El segundo hijo del objetivo",
"duration": "24:10"
}
]
},
"Attack on Titan": {
"Temporada 3": [
{
"cap": 46,
"name": "La reina de la muralla",
"duration": "23:55"
},
{
"cap": 54,
"name": "Héroe",
"duration": "23:55"
}
],
"Temporada 4":[
{
"cap": 60,
"name": "Al otro lado del mar",
"duration": "23:55"
},
{
"cap": 72,
"name": "Los hijos del bosque",
"duration": "23:55"
}
]
}}
historial = []
new_watch = {}
count = 0
run = ''
print ('\nBienvenido a Anima-te-ve!')
while run != '3':
    print('\nQue deseas realizar hoy?')
    run = input('Puedes elegir entre: \n1. Seleccionar una serie a ver\n2. Ver el historial\n3. Salir\nColoca el numero de la opcion que prefieres: ')
    if run != '1' and run != '2' and run != '3':
        print ('\nIngreso invalido')
        continue

    elif run == '1':
        # Series Disponibles
        print ('\nSeries disponibles:')
        for key,v in anime.items():
            print (key)
        serie = input ('\nIndica el nombre de la serie que desees ver tal y como se muestra en pantalla:\n>>')
        while serie not in anime.keys():
            serie = input ('\nIndica el nombre de la serie que desees ver tal y como se muestra en pantalla:\n>>')
       
        # Temporadas
        temporadas = anime[serie]
        print('\nTemporadas disponibles:') 
        for season in temporadas:
            print (season)
        season = input('\nElige entre las temporadas disponibles para observar su lista de capitulos:\n(Ej. Temporada 1)\n>>')
        while season not in temporadas:
            season = input('\nElige entre las temporadas disponibles para observar su lista de capitulos:\n(Ej. Temporada 1)\n>>')
       
        # Capitulos
        print('\nCapitulos disponibles:')
        for season, cap in temporadas.items():
            for caps in cap:
                print (caps)
        while True:
            try:
                capitulo = int(input('\nIndica el numero del capitulo que deseas ver:\n>>'))
                break
            except:
                print ('Por favor ingrese un capitulo valido.')
                continue 

        # Informacion del capitulo
        for season, cap in temporadas.items():
            for capss in cap:
                for key, values in capss.items():
                    if key == 'cap':
                        if values == capitulo:
                            cap_key = capss
                            print ('\nCapitulo a ver:',capss)
                            historial.append(capss)
                            count += 1
                        else:
                            print ('Capitulo no disponible.')
        continue

    elif run == '2':
        # Imprimir historial y cantidad de capitulos
        historial.reverse()
        print ('\nUsted ha visto un total de', count,'capitulos.')
        print ('Su historial de reproduccion es', historial)

    elif run == '3':
        print ('\nHasta pronto!')

    