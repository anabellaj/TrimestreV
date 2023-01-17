# Facturas, se puede agregar, eliminar o pagar factura. Despues de cada operacion mostrar cantidad 
# cobrada y cantidad pendiente.

facturas = {}
cobrado = 0
pendiente = 0
run = ''
while run != 'T':
    run = input('\nIngrese "A" para agregar una factura, "P" para pagar una factura o "T" para terminar\n>>').title()
    while run != 'A' and run != 'T' and run != 'P':
        run = input('\nIngrese "A" para agregar una factura, "P" para pagar una factura o "T" para terminar\n>>').title()
    if run == 'A':
        numero = input('\nIngrese el id de la factura: ')
        while numero in facturas:
            print('Ya existe una factura con ese nombre.')
            numero = input('Por favor ingrese el id de la factura nueva: ')
        coste = input('Ingrese el monto de la factura: ')
        while not coste.isnumeric():
            coste = input('Ingrese el monto de la factura: ')
        coste = float(coste)
        facturas[numero] = coste
        pendiente += coste
    if run == 'P':
        numero = input('Ingrese el id de la factura a pagar\n>>')
        while not numero in facturas:
            print ('No existe una factura con ese nombre.')
            numero = input('Ingrese el id de la factura a pagar\n>>')
        coste = facturas.pop(numero)
        cobrado += coste
        pendiente -= coste
    print ('\nMonto recaudado:', cobrado)
    print ('Monto pendiente:', pendiente)