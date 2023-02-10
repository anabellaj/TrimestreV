def suma(x, y):
    return int(x) + int(y)
def resta (x,y):
    return int(x) - int(y)
def multiplicacion (x,y):
    return int(x) * int(y)
def division(x,y):
    return int(x)/ int(y)

def get_parameters ():
    while True:
        try:
            x = int(input('Ingrese el primer numero:\n>> '))
            y = int(input('Ingrese el segundo numero:\n>> '))
            break
        except:
            print('Recuerde ingresar unicamente numeros enteros')
    return x,y

def main():
    while True:
        selection = input('\nBienvenido a  la calculadora\n\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Salir\n\n>> ')
        while not selection.isnumeric() or int(selection) not in range (1,6):
            selection = input('ERROR - Opcion Invalida\nPor favor vuelva a intentar\n\nBienvenido a  la calculadora\n\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Salir\n\n>> ')
        selection =  int(selection)
        if selection == 1:
            print ('SUMA')
            x,y = get_parameters()
            print ('La suma es igual a', suma(x,y))
        elif selection == 2:
            print ('RESTA')
            x,y = get_parameters()
            print ('La resta es igual a', resta(x,y))
        elif selection == 3:
            print ('MULTIPLICACION')
            x,y = get_parameters()
            print ('La multiplicacion es igual a', (multiplicacion(x,y)))
        elif selection == 4:
            print ("DIVISION")
            x,y = get_parameters()
            print ('La division es igual a', division(x,y))
        elif selection == 5:
            print('Hasta pronto')
            break
main()