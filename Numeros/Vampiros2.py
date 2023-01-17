# Dos numeros multiplicados, que contiene los mismos digitos que el numero original, dan como resultado
# el numero original (ej. 2160: 21 * 60)

num = input('Please enter a number: ')
while not num.isnumeric():
    num = input('Please enter a number: ')
num = int(num)

divisores = []
for n in range(1, num+1):
    if num%n == 0:
        if str(n) in str(num):
            divisores.append(n)
# mult = 1
# for divisor in divisores:


# if mult == int(num):
#     print (f'El numero {num} es un numero vampiro.')
# else:
#     print (f'El numero {num} no es un numero vampiro.')