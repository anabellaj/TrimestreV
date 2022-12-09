#Un numero narcicista es aquellos cuya suma de sus digitos elevados cada uno a la longitud del numero
# es igual al numero original

numero_og = input('Please enter a number: ')
while numero_og.isnumeric() == False:
    numero_og = input('Please enter a number: ')
if numero_og.isnumeric() == True:
    numero = str(numero_og)

length = len(numero)
length = int(length)

suma = 0
for cifra in numero:
    dig = int(cifra)
    elevado = dig**length
    suma = suma + elevado

if str(suma) == numero_og:
    print (f'El numero {numero_og} es narcicista.')
else:
    print (f'El numero {numero_og} no es narcicista.')







