# Una lista dentro de otra se recorre como una matriz.
secciones = [['Maria','Andres', 'Pedro'],['Stefania','Gabriel','Julia','Manuel']]
for seccion in secciones:
    for estudiante in seccion:
        print (f'El nombre del estudiante es {estudiante}.')

# Segunda forma
for i in range(len(secciones)):
    for j in range(len(secciones[i])):
        print (f'El nombre de estudiantes es {secciones[i][j]}')
