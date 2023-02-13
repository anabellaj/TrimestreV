# Dar una lista y devolver la suma acumulada
def get_numeros():
    lista = []
    contador = 1
    while True:
        try:
            numeros = int(input(f'Ingrese el numero {contador} de la lista:\n>> '))
            contador += 1
            lista.append(numeros)
            if input('Presione cualquier tecla para ingresar otro numero o X para ver la suma acumulada\n>> ').title() =='X':
                break
        except:
            print('ERROR - Por favor solo ingrese numeros enteros')
    return lista

def main():
    suma = []
    sumas = 0
    n = 0
    contador = 0
    lista = get_numeros()
    for numero in lista:
        if contador == 0:
            suma.append(numero)
            n = numero
        else:
            sumas += n + numero
            n = 0
            suma.append(sumas)
        contador += 1
    print ('Suma acumulada:', suma)
main()    

            
            
            
            
        