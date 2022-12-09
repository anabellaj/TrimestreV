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
        num = input('Please enter a number with a pair number of digits: ')
num = int(num)

# Factorizar numero
divisores = []
for divisor in range(1, num+1):
    if num%divisor == 0:
        divisores.append(divisor)

# Mitad de digitos y no ceros finales
dvalidos = []
for divisor in divisores:
    if len(str(divisor)) == len(str(int(num/2))):
        dvalidos.append(divisor)
for dv in dvalidos:
    if int(dv)%10 == 0:
        dvalidos.remove(dv)
    
print (dvalidos)





