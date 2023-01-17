# Imprimir resto y cociente

num1 = input('Please enter a number: ')
while not num1.isnumeric():
    num1 = input('Please enter a number: ')
num2 = input('Please enter a number: ')
while not num2.isnumeric():
    num2 = input('Please enter a number: ')

num1 = int(num1)
num2 = int(num2)

cociente = num1/num2
resto = num1%num2

print (f'La division de {num1} entre {num2} da como cociente {cociente} y su resto es {resto}.')