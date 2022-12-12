# Es el resultado de la suma de n numeros naturales en serie de 3 (1,4,7,10) ej: 1,5,12,22...

num = input('Please enter a number: ')
while not num.isnumeric():
    num = input('Please enter a number: ')
num = int(num)

contador = 1
suma = 0
while num >= contador:
    suma += contador
    contador += 3
    if suma == num:
        print(f'{num} es pentagonal.')
        break
    if suma > num:
        print(f'{num} no es pentagonal.')
        break