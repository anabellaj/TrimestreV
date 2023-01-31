# Chequear si todos los digitos de un numero son iguales
# Ver si la suma de sus digitos da un numero cuadrado
while True:
    try:
        num = int (input('\nPlease enter any integer number to check whether it is repunit or not:\n>>'))
        break
    except:
        print ('\nPlease enter a valid integer number')
        continue

#Repunit
repunit = False
for n in str(num):
    repeticiones = str(num).count(n)
    if repeticiones == len(str(num)):
        repunit = True

#Suma da numero cuadrado perfecto
cuadrado = False
suma = 0
for n in str(num):
    suma += int(n)
if float(suma ** 0.5)%int(suma**0.5) == 0:
    cuadrado = True 

if cuadrado == True and repunit == True:
    print (f'\nThe number {num} is a repunit number and the sum of its digits results in a square number.')
elif cuadrado == False and repunit == False:
    print (f'\nThe number {num} is not a repunit number and the sum of its digits doesnt equal a square number.')
elif cuadrado == True and repunit == False:
    print (f'\nThe number {num} is not a repunit number but the sum of its digits equals a square number.')
elif cuadrado == False and repunit == True:
    print (f'\nThe number {num} is a repunit number but the sum of its digits doesnt equal a square number.')
