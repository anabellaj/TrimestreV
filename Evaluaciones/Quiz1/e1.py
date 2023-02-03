while True:
    try:
        number=int(input('Por favor ingrese un numero eentero entre 2 y 12:\n>>> '))
        if number > 12 or number < 2:
                print ('ERROR: Ingreso Invalido\n')
                number=int(input('Por favor ingrese un numero eentero entre 2 y 12:\n>>> '))
        else:
            break
    except:
        print ('ERROR: Ingreso Invalido\n')
print (f'Combinaciones para el numero {number}')
lista_numeros = [2,3,4,5,6,7,8,9,10,11,12]
for n in lista_numeros:
    for x in range(2,13):
        if n + x == number:
            print (n, x)

