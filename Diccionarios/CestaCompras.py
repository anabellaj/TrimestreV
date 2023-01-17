# Agregar articulos a la cesta y finalmente imprimir el total
compras = {}
run = True
total = 0
while run == True:
    articulo = input('\nQue articulo desea agregar a la lista?\n>> ').title()
    precio = input ('\nIndique el precio del articulo\n>> ')
    while not precio.isnumeric():
        precio = input ('\nIndique el precio del articulo\n>> ')
    compras [articulo] = float(precio)
    go = input('\nDesea agregar mas articulos?\n>>Indique si o no:\n>> ').title()
    while go != 'Si' and go != 'No':
        go = input('\nDesea agregar mas articulos?\n>>Indique si o no\n>> ').title()
    if go == 'Si':
        continue
    elif go == 'No':
        print('\nLista de Compras\n')
        for articulo, precio in compras.items():
            total += precio
        for articulo, precio in compras.items():
            print (articulo, '.....', precio)
        print ('\nCosto total .....', total)       
    run = False

