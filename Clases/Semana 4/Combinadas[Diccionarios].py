# Listas de Diccionarios
elementos = [{
    'nombre': 'hidrogeno',
    'numero': 1, 
    'peso': 1.00794,
    'simbolo': 'H'
    },
    {
        'nombre': 'helio',
        'numero':2,
        'peso': 4.002602,
        'simbolo':'He'
    }]
# Cada diccionario es un elemento de la lista grande
for elemento in elementos:
    print (f"Nombre: {elemento['nombre']} - Simbolo: {elemento['simbolo']}")