while True:
    while True:
        try:
            n = int(input('Ingrese un numero para verificar si pertenece a la serie de Fibonacci:\n>> '))
            break
        except:
            print('ERROR\nPor favor ingrese unicamente numeros enteros')
    term1 = 0
    term2 = 1
    count = 0
    fibonacci = []
    while count < n:
        fibonacci.append(term1)
        new_term = term1 + term2
        term1 = term2
        term2 = new_term
        count += 1
    if n in fibonacci:
        print(f'El numero {n} si pertenece a la serie de Fibonacci.')
    else:
        print(f'El numero {n} no pertenece a la serie de Fibonacci.')
    if input('Presione X para salir o cualquier tecla para continuar:\n>> ').title() == 'X':
        break
    
    