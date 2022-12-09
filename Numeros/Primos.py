num = input('Please enter a number: ')
while num.isnumeric() == False:
    num = input('Please enter a number: ')
num = int(num)

contador = 0
for divisor in range(1, num+1):
    if (num%divisor) == 0:
        contador += 1
    else:
        pass

if contador == 2:
    print(f'El numero {num} es primo.')
else:
    print(f'El numero {num} no es primo.')