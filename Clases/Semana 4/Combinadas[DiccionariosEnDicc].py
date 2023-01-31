
elementos = {'Hidrogeno':{
    'numero': 1, 
    'peso': 1.00794,
    'simbolo': 'H'
    },
    'Helio':{
    'numero':2,
    'peso': 4.002602,
    'simbolo':'He'}
    }

for k, v in elementos.items():
    print ('\nNombre:',k)
    for k, v in v.items():
        if k == 'numero':
            print ('Numero:',v)
        elif k == 'peso':
            print ('Peso:', v)
        elif k == 'simbolo':
            print ('Simbolo:',v)

# Cambiar elementos de un diccionario dentro de otro
elementos['Hidrogeno']['numero'] = 7
for k, v in elementos.items():
    print ('\nNombre:',k)
    print (f"Numero: {v['numero']} - Peso: {v['peso']} - Simbolo: {v['simbolo']}")


