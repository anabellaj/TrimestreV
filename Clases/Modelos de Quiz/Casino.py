# Camarada vs Ondulado
# Seleccionar rol
import random
print ('\nBienvenido al casino!')
rol = input('Por favor ingrese su rol:\n1. Camarada\n2. Ondulado')
while rol not in ['1', '2']:
    print ('Recuerde colocar solamente el numero correspondiente a su opcion.')
    rol = input('Por favor ingrese su rol:\n1. Camarada\n2. Ondulado')
run = ''
while run != 'E':
    while True:
        number = random.randint(100, 999)
        # Camarada
        camarada = []
        if len(camarada) < 3:
            for n in str(number):
                repeticiones = str(number).count(n)
                if repeticiones == len(str(number)):
                    camarada.append(number)
                    continue
            
        # Ondulados
        ondulados = []
        ondulado = True
        count = 0
        if len(ondulados) < 3:
            even_index = list(str(number))[0]
            odd_index = list(str(number))[1]
            if even_index == odd_index:
                ondulado = False
            else:
                for x in str(number):
                    if (count+2)%2 == 0:
                        if x != even_index:
                            ondulado = False
                        count +=1
                    elif (count+2) %2 !=0:
                        if x != odd_index:
                            ondulado = False
                        count += 1
            if ondulado == True:
                ondulados.append(number)
                continue
        if len (camarada) ==3 and len (ondulados) == 3:
            break

    suma_camarada = 0
    for element in camarada:
        suma_camarada += int(element)
    suma_ondulado = 0
    for element in ondulados:
        suma_ondulado += int(element)

    if suma_camarada > suma_ondulado:
        if rol == 1:
            print (f'Has ganado con los numeros camaradas. Tu puntuacion fue de {suma_camarada}.\nLos numeros ondulados perdieron con una puntuacion de {suma_ondulado}.')
        else:
            print (f'Has perdido con los numeros ondulados. Tu puntuacion fue de {suma_ondulado}.\nLos numeros camaradas ganaron con una puntuacion de {suma_camarada}.')
    elif suma_ondulado > suma_camarada:
        if rol == 2:
            print (f'Has ganado con los numeros ondulados. Tu puntuacion fue de {suma_ondulado}.\nLos numeros camaradas perdieron con una puntuacion de {suma_camarada}.')
        else: 
            print (f'Has perdido con los numeros camaradas. Tu puntuacion fue de {suma_camarada}.\nLos numeros ondulados ganaron con una puntuacion de {suma_ondulado}.')

    run = input('\n\nPulse "E" para salir o cualquier tecla para continuar\n>>')

print ('Esperamos que hayas disfrutado! Hasta pronto.')
