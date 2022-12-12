# número natural compuesto con un número par de dígitos, que se puede factorizar en dos números naturales 
# cada uno con la mitad de dígitos que el número original y no ambos con ceros finales, donde los dos factores 
# contienen precisamente todos los dígitos del número original, sin importar su orden

num = input('Please enter a number with a pair number of digits: ')
while not num.isnumeric():
    num = input('Please enter a number with a pair number of digits: ')

# Verficar num par de digitos 
length = len(num)
verify = length%2
while verify != 0:
    num = input('Please enter a number with a pair number of digits: ')
    while not num.isnumeric():
        num = input ('Please enter a number with a pair number of digits: ')
    verify = len(num)%2
num = int(num)

# Factorizar numero
divisores = []
for divisor in range(1, num+1):
    if num%divisor == 0:
        divisores.append(divisor)

# Mitad de digitos y no ceros finales
dvalidos = []
for divisor in divisores:
    if len(str(divisor)) == len(str(num))/2:
        dvalidos.append(divisor)
finald = []
for dv in dvalidos:
    if int(dv)%10 != 0:
        finald.append(dv)

# Digitos en el numero original
dfinales = []
listanum = []
for digito in str(num):
    listanum.append(digito)

for dv in dvalidos:
    if str(dv) in listanum:
        dfinales.append(dv)

# Multiplicacion
product = 1
for x in dfinales:
    product *= x
else: 
    pass

if product == num:
    print (f'{num} es un numero vampiro.')
else:
    print(f'{num} no es un numero vampiro.')







