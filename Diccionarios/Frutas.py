# Mercado de frutas. Pedir la fruta y los kilos e imprimir el precio final.

frutas = {
    'Platano': 1.35,
    'Manzana':	0.80,
    'Pera':	0.85,
    'Naranja':	0.70
}
while True:
    fruta = input('Que fruta desea ordenar?\nPuede elegir entre platano, manzana, pera o naranja\nIngrese el nombre de la fruta: ')
    fruit = fruta.title()
    if fruit in frutas:
        pass
    else: 
        print (f'\n{fruta.title()} no esta disponible. Eliga de la lista de frutas indicadas.')
        continue
    kilos = input(f'\nCuantos kilos de {fruta.lower()} desea?\n>> ')
    while not kilos.isnumeric():
        kilos = input(f'\nCuantos kilos de {fruta.lower()} desea?\n>> ')
    kilos = float(kilos)
    break

print ('\n',int(kilos), 'kg de', fruit.lower(), 'valen', frutas[fruit]*kilos,'$')