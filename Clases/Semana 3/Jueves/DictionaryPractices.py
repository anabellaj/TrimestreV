# Estructura de datos que permite almacenar cualquier variable como value e 
# identificar a cada uno de ellos a traves de un Key. Estructura = {key:value}

dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print (dict['model'])      #Siempre que coloquemos el key, nos devuelve el value que le corresponda. 
print (dict.get('model'))
dict['year'] = 2020
print (dict['year'])
dict.update({'color':'red'})
print (dict)