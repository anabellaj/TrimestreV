# Generar diccionario con la info del directorio, donde k=nif y value otro diccionario con toda la info. 
# Las lineas estan separadas con \n y la primera linea contiene los nombres de los campos

datos = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
info = datos.split('\n')

directorio = {}

# Lista campos
lista_campos = info[0].split(';')

for dato in info[1:]:
    cliente = {}
    lista_info = dato.split(';')
    for info in range(1,len(lista_campos)):
        if lista_campos[info] == 'descuento':
            lista_info[info] = float (lista_info[info])
        cliente[lista_campos[info]] = lista_info[info]
    directorio[lista_info[0]] = cliente
print (directorio)