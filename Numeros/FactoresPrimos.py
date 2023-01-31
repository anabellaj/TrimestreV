# Determinar si un numero que sea producto de la multiplciacion de numeros pares
number = input('Welcome!\nPlease enter an integer number:\n>>')
while not number.isnumeric():
    number = input('Welcome!\nPlease enter an integer number:\n>>')
factores = []
for n in range(1, int(number)+1):
    if int(number) % n == 0:
        factores.append(n)
primos = []
for x in factores:
    count = 0
    for y in range(1, int(x)+1):
        if x % y == 0:
            count +=1
    if count == 2:
        primos.append(x)
product = 1 
for j in primos:
    product *= 1
    if product < int(number):
        product *= j
if product == int(number):
    print (f'El numero {number} es el resultado de la multiplicacion de factores primos.')
else:
    print (f'El numero {number} no es el producto de factores primos.')