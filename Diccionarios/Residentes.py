residentes = {"Julia Rodríguez": {"Edad": 21, "Género": "M", "Ocupación": "Estudiante"}, "Santiago López": {"Edad": 33, "Género": "H", "Ocupación": "Abogado"}, "Luis González": {"Edad": 8, "Género": "H", "Ocupación": "Estudiante"}, "Luisana González": {"Edad": 5, "Género": "M", "Ocupación": "Estudiante"}, "Martina Reverón de González": {"Edad": 37, "Género": "M", "Ocupación": "Ingeniero"}, "Sergio González": {"Edad": 37, "Género": "H", "Ocupación": "Ingeniero"}, "Abel Araujo": {"Edad": 81, "Género": "H", "Ocupación": "Médico"}, "Roberto Mendoza": {"Edad": 56, "Género": "H", "Ocupación": "Profesor"}, "Bárbara Zapatero de Piñera": {"Edad": 32, "Género": "M", "Ocupación": "Psicólogo"}, "Leonardo Piñera": {"Edad": 31, "Género": "H", "Ocupación": "Administrador"}, "Gustavo Álvarez": {"Edad": 14, "Género": "H", "Ocupación": "Estudiante"}, "Guillermo Álvarez": {"Edad": 38, "Género": "H", "Ocupación": "Médico"}, "Laura Paz de Álvarez": {"Edad": 38, "Género": "M", "Ocupación": "Desempleado"}, "Ignacio Salcedo": {"Edad": 19, "Género": "H", "Ocupación": "Estudiante"}, "Saúl Salcedo": {"Edad": 22, "Género": "H", "Ocupación": "Estudiante"}, "Romina Salcedo": {"Edad": 25, "Género": "M", "Ocupación": "Administrador"}, "Elena Pinto de Salcedo": {"Edad": 52, "Género": "M", "Ocupación": "Abogado"}, "Mauricio Salcedo": {"Edad": 52, "Género": "H", "Ocupación": "Ingeniero"}, "Tatiana Echeverría": {"Edad": 68, "Género": "M", "Ocupación": "Médico"}, 'Marcelo Gonçalves': {"Edad": 27, "Género": "H", "Ocupación": "Administrador"}, "Jessica Franco de Gonçalves": {"Edad": 26, "Género": "M", "Ocupación": "Profesor"}, "Valerio Fiore": {"Edad": 97, "Género": "H", "Ocupación": "Desempleado"}, "Giuliana Rossi de Fiore": {"Edad": 95, "Género": "M", "Ocupación": "Desempleado"}, "José Castro": {"Edad": 35, "Género": "H", "Ocupación": "Abogado"}, "Samantha Correa de Castro": {"Edad": 35, "Género": "M", "Ocupación": "Abogado"}, "Ángel Castro": {"Edad": 7, "Género": "H", "Ocupación": "Estudiante"}, "Antonieta Marín": {"Edad": 58, "Género": "M", "Ocupación": "Profesor"}, "Lorenzo Blanco": {"Edad": 77, "Género": "H", "Ocupación": "Abogado"}, "Vanessa Blanco de Bustamante": {"Edad": 37, "Género": "M", "Ocupación": "Médico"}, "Raúl Bustamante": {"Edad": 39, "Género": "H", "Ocupación": "Médico"}, "Carolina Alcalá": {"Edad": 24, "Género": "M", "Ocupación": "Ingeniero"}, "Juan Alcalá": {"Edad": 60, "Género": "H", "Ocupación": "Psicólogo"}, "Ingrid Gil de Alcalá": {"Edad": 60, "Género": "M", "Ocupación": "Profesor"}, "Francesca Costa de Gil": {"Edad": 88, "Género": "M", "Ocupación": "Médico"}, "Giancarlo Gil": {'Edad': 89, "Género": "H", "Ocupación": "Psicólogo"}, "César Lovera": {"Edad": 64, "Género": "H", "Ocupación": "Administrador"}, "Natalia Lovera": {"Edad": 64, "Género": "M", "Ocupación": "Desempleado"}}
# Cantidad total de residentes
print ('Cantidad total de residentes:', len(residentes.keys()))
# Promedio de edad por genero
mujeres, hombres, total_edadM, total_M,total_H, total_edadH= 0,0,0,0,0,0
for k,v in residentes.items():
    for carac, value in v.items():
        if value == 'M':
            total_edadM += v['Edad']
            total_M += 1
        elif value == 'H':
            total_edadH+= v['Edad']
            total_H += 1
promedioM, promedioH = total_edadM/total_M, total_edadH/total_H
print('Promedio de edad de las mujeres:',int(promedioM),'Promedio de edad de los hombres',int(promedioH))
# Persona mas joven y mas vieja
min,max = 100,0
for k,v in residentes.items():
    if v["Edad"] > max:
        max = v["Edad"]
    if v["Edad"]<min:
        min =v["Edad"]
for k,v in residentes.items():
    if v["Edad"] == max:
        print(f'La persona mas vieja es {k} y su edad es de {v["Edad"]}')
    if v["Edad"] == min:
        print(f'La persona mas joven es {k} y su edad es de {v["Edad"]}')
# Cantidad de personas por ocupacion
