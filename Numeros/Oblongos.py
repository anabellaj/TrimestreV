while True:
    oblongo = False
    try:
        number =int(input('Por favor ingrese un numero entero para chequear si es oblongo:\n>> '))
        break
    except:
        print('ERROR\nRecuerde ingresar unicamente numeros enteros')
for n in range(1,number+1):
    if n*(n+1) == number:
        oblongo = True   
if oblongo:
    print(f'El numero {number} es un numero oblongo.')
else:
    print(f'El numero {number} no es un numero oblongo.')
