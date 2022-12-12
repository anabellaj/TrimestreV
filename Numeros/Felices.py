# Un numero feliz cumple que al elevar cada una de sus cifras al cuadrado y sumar los digitos del resultado
# (cada uno al cuadrado) entre ellos, y repitiendo hasta que el resultado de la suma sea de una cifra. Si
# dicho resultado final es 1 se cumple que es un numero feliz, si no es 1 entonces es infeliz.

numog = input('Please enter a number: ')
while not numog.isnumeric():
    numog = input('Please enter a number: ')

num = numog
suma = 0
while True:
    for digito in str(num):
        digito = int(digito) ** 2
        suma += int(digito)
    num = suma
    if len(str(num)) == 1:
        break
    suma = 0

if suma == 1:
    print(f'{numog} es un numero feliz.')
else:
    print(f'{numog} es un numero infeliz.')