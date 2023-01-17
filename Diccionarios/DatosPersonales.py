# Preguntar al usuario nombre, edad, direccion y telefono. Guardar en un diccionario e imprimir.

nombre = input('Por favor ingrese su nombre:\n>')
edad = input('Por favor ingrese su edad:\n>')
direccion = input ('Por favor ingrese su direccion de residencia:\n>')
telefono = input('Por favor ingrese su numero telefonico:\n>')

datos = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

print (datos['nombre'],'tiene', datos['edad'], 'años, vive en', datos['direccion'], 'y su numero de telefono es', datos['telefono'] +'.')