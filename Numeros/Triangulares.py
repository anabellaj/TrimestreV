# Es el resultado de la suma de n numeros naturales consecutivos (ej. 1,3,6,10)

num = input('Please enter a number: ')
while not num.isnumeric():
    num = input('Please enter a number: ')
num = int(num)

contador = 1
suma = 0
while num >= contador:
    suma += contador
    contador += 1
    if suma == num:
        print(f'{num} es triangular.')
        break
    if suma > num:
        print(f'{num} no es triangular.')
        break
