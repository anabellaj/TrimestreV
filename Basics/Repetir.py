# Ingresar nombre y numero, imprimir nombre tantas veces como el numero indique

nombre = input('Please enter your name: ')
while nombre.isnumeric():
    nombre = input('Please enter your name:')

num = input('Please enter a number: ')
while not num.isnumeric():
    num = input('Please enter a number: ')
num = int(num)

contador = 0
while contador < num:
    print (f'{nombre}')
    contador += 1