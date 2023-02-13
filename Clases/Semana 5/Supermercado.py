
def inventario(datasets):
    for k, v in datasets.items():
        print ('\nSector:', k)
        for product in v:
            print (f"\tProducto: {product['Producto']} - Precio: {product['Precio']} - IVA: {product['IVA']} - Cantidad disponible: {product['Inventario']}")

def descuentos(cedula):
    abundantes, palindromos = True,True
    suma = 0
    for divisor in range(1, cedula):
        if (cedula % divisor) == 0:
            suma += divisor
    if suma > cedula:
        abundantes = True
    if str(cedula) == str(cedula)[::-1]:
        palindromos = True
    if abundantes or palindromos:
        return True
    else:
        return False

def compra(datasets):
    while True:
        try:
            nombre = input('Por favor ingrese su nombre completo:\n>> ')
            if nombre.isnumeric():
                raise Exception
            break
        except:
            print('\nERROR - Ingreso invalido\nRecuerde ingresar su nombre y apellido, sin caracteres especiales')
    while True:
        try:
            cedula = int(input('Por favor ingrese su cedula (sin puntos):\n>> '))
            break
        except:
            print('\nERROR - Ingreso invalido')
    while True:
        try:
            telefono = int(input('Por favor ingrese su numero de telefono (sin puntos):\n>> '))
            if len(str(telefono)) not in range(9,12):
                raise Exception
            break
        except:
            print('ERROR - Ingreso invalido\nRecuerde solo ingresar numeros y que su numero de telefono debe tener entre 9 y 11 digitos')
    cliente = {'nombre': nombre,'cedula': cedula, 'telefono':telefono}
    compare= 0
    index, indice = 0,0
    producto,key = '', ''
    while True:
        try:
            print('\t------------PRODUCTOS DISPONIBLES-------------')
            inventario(datasets)
            producto = input('Ingrese el nombre del producto a comprar:\n>> ').title()
            for tienda, value in datasets.items():
                index = 0
                for v in value:
                    for carac, valor in v.items():
                        if producto == valor:
                            key = tienda
                            compare+=1
                            indice = index
                    index += 1
            if compare != 1:
                raise Exception
            break
        except:
            print(f'El producto {producto} no se encuentra disponible.')
    while True:
        try:
            amount = int(input('Indique la cantidad del producto que desee:\n>> '))
            if amount > datasets[key][indice]['Inventario']:
                raise Exception
            break
        except:
            print('\n ERROR - Debe ingresar un valor menor o igual a la cantidad disponible del mismo')
    datasets[key][indice]['Inventario'] -= amount
    precio = datasets[key][indice]['Precio'] * amount
    if datasets[key][indice]['IVA'] == True:
        precio += precio*0.16
    discount = descuentos(cedula)
    if discount== True:
        precio -= precio*0.1
        orden = {'Producto': producto, 'Cantidad': amount, 'Monto': precio, 'Descuento': 'Se ha aplicado un descuento del 10%'}
    else:
        orden = {'Producto': producto, 'Cantidad': amount, 'Monto': precio}
    cliente.update({'Orden': orden})
    return cliente

def factura(cliente):
    print ('\n\t---------------FACTURA----------------')
    print(f"Nombre: {cliente['nombre']}\nCedula: {cliente['cedula']}\nNumero de telefono: {cliente['telefono']}\nProducto comprado: {cliente['Orden']['Producto']} - Cantidad: {cliente['Orden']['Cantidad']}\nMonto total a pagar: {cliente['Orden']['Monto']}$")
    for k, v in cliente.items():
        if 'Orden' == k:
            if 'Descuento' in v.keys():
                print('Se ha aplicado un descuento del 10%')
        
def main():
    datasets = {
        'Charcutería': [{ 'Producto': 'Carne', 'Precio': 20, 'IVA':False, 'Inventario':5 }, 
                        { 'Producto': 'Pollo','Precio': 15, 'IVA': False, 'Inventario':4 }],
        'Panadería': [{ 'Producto': 'Pan', 'Precio': 5, 'IVA':True, 'Inventario':10 },
                      { 'Producto': 'Cachito','Precio': 8, 'IVA': True, 'Inventario':6 },
                      { 'Producto': 'Torta', 'Precio': 7, 'IVA':True, 'Inventario':3 }],
        'Pescaderia': [{ 'Producto': 'Mero', 'Precio': 10, 'IVA':True, 'Inventario':7 }, 
                       { 'Producto': 'Salmón', 'Precio':25,'IVA': True,'Inventario':5 }]
                }
    while True:
        while True:
            try: 
                run = int(input('\n---------BIENVENIDO AL SUPERMERDADO----------\nQue desea relizar hoy?\n\nPresione 1 para ver el inventario\nPresione 2 para comprar un producto\nPresione 3 para salir\n>> '))
                if run not in range(1,4): 
                    raise Exception
                break
            except:
                print('\nERROR - OPCION INVALIDA')
        if run == 1:
            # Ver inventario
            print ('\n-------INVENTARIO--------')
            inventario(datasets)
        elif run == 2:
            # Hacer orden
            cliente = compra(datasets)
            factura (cliente)
        elif run ==3:
            print('Hasta pronto!')
            break
main()