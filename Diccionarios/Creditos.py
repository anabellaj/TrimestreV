# Imprimir los creditos de cada asignatura y los creditos totales

asignaturas = {
    'Matemáticas': 6, 'Física': 4, 'Química': 5
}

for k, v in asignaturas.items():
    print ('La asignatura', k.lower(), 'tiene', v, 'creditos.')
suma = 0
for k, v in asignaturas.items():
    suma += v
print (f'El curso tiene un total de {suma} creditos.')