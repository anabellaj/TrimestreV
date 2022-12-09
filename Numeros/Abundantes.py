# La suma de sus divisores (menos el mismo) es mayor al numero original

num = input('Please enter a number: ')
while num.isnumeric() == False:
    num = input('Please enter a number: ')
num = int(num)

suma = 0
for divisor in range(1, num):
    if (num % divisor) == 0:
        suma += divisor

if suma > num:
    print(f'El numero {num} es abundante.')
else:
    print(f'El numero {num} es deficiente.')
