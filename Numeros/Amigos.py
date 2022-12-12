# Dos numeros son amigos si cada uno se obtiene sumando los divisores del otro

num1 = input('Please enter a number: ')
num2 = input('Please enter another number: ')
while not num1.isnumeric() or not num2.isnumeric():
    num1 = input('Please enter a number: ')
    num2 = input('Please enter another number: ')
num1 = int(num1)
num2 = int(num2)

# Suma divisores num 1
suma1 = 0
for digito in range(1, num1):
    if (num1 % digito) == 0:
        suma1 += digito

# Suma divisores num 2
suma2 = 0
for digito in range(1,num2):
    if (num2 % digito) == 0:
        suma2 += digito

if suma1 == num2 and suma2 == num1:
    print(f'Los numeros {num1} y {num2} son amigos.')
else: 
    print(f'Los numeros {num1} y {num2} no son amigos.')