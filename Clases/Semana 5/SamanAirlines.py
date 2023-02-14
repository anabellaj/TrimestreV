def pilotos(aviones):
    while True:
        try: 
            cedula = int(input('Por favor ingrese su cedula:\n>> '))
            break
        except:
            print('\nERROR - Ingreso Invalido\nRecuerde solo insertar numeros (sin puntos!)')
    for avion in aviones.keys():
        print ('Tipo de avion:',avion)
    while True:
        try:
            tipo = int(input('\nQue tipo de avion vuela ud.?\nIngrese 1 para seleccionar HELICE\nIngrese 2 para seleccionar JET\n>> '))
            if tipo not in range(1,3):
                raise Exception
            break
        except:
            print('\nERROR - Opcion Invalida\nIngrese 1 o 2 dependiendo de su seleccion')
    if tipo == 1:
        tipo = 'Helice'
    else:
        tipo = 'Jet'
    while True:
        try:
            horas = int(input('Ingrese la cantidad de horas voladas:\n>> '))
            break
        except:
            print('\nERROR - Por favor ingrese unicamente numeros enteros')
    costo = aviones[tipo] * horas
    bono = False
    if horas > 8:
        costo += costo*0.1
        bono = True
        piloto ={'Cedula de identidad:': cedula, 'Tipo de avion:': tipo, 'Cantidad de horas voladas': horas, 'Monto a pagar:': costo, 'Aumento aplicado:': 'si'}
    else:
        piloto ={'Cedula de identidad:': cedula, 'Tipo de avion:': tipo, 'Cantidad de horas voladas': horas, 'Monto a pagar:': costo}
    return piloto

def todos_pilotos(pilots):
    contador = 1
    for piloto in pilots:
        print('\n---------INFORMACION DEL PILOTO #',contador,'------------')
        for k,v in piloto.items():
            print (k, '->', v)
        contador += 1 
    print('\nCantidad total de pilotos:', len(pilots))

def stats(pilots):
    xjets, xhelice, discounted = [],[],[]
    for piloto in pilots:
        if piloto['Tipo de avion:'] == 'Helice':
            xhelice.append(piloto)
        elif piloto['Tipo de avion:'] =='Jet':
            xjets.append(piloto)
        if 'Aumento aplicado:' in piloto.keys():
            discounted.append(piloto)
    print('\n-----ESTADISTICAS DEL DIA-------\nCantidad de pilotos de aviones tipo jet:', len(xjets),'pilotos', '\nCantidad de pilotos de aviones tipo helice:', len(xhelice),'pilotos','\nCantidad de pilotos con aumento del 10%:', len(discounted),'pilotos')
    montoj, montoh = 0,0
    for j in xjets: 
        montoj += j['Monto a pagar:']
    if len(xjets)!=0:
        promedioj = montoj/len(xjets)
    else:
        promedioj = 0
    for h in xhelice:
        montoh += h['Monto a pagar:']
    if len(xhelice)!=0:
        promedioh = montoh/len(xhelice)
    else:
        promedioh = 0
    print('Promedio de pago para aviones tipo helice:', promedioh,'$','\nPromedio de pago para aviones tipo jet:',promedioj,'$')
    
def main():
    aviones = {'Helice':40, 'Jet':50}
    pilots = []
    while True:
        print('\n----------BIENVENIDO A SAMAN AIRLINES-----------')
        while True:
            try: 
                run = int(input('Presione 1 para ingresar un piloto\nPresione 2 para mostrar todos los pilotos\nPresione 3 para mostrar las estadisticas del dia\nPresione 4 para salir\n>> '))
                if run not in range(1,5):
                    raise Exception
                break
            except:
                print('\nERROR - Opcion Invalida\nPor favor ingrese un numero entre el 1 y el 3 dependiendo de su eleccion')
        if run == 1:
            piloto = pilotos(aviones)
            pilots.append(piloto)
        elif run == 2:
            todos_pilotos(pilots)
        elif run ==3:
            stats(pilots)
        elif run ==4:
            print('\nHasta pronto!\n\n')
main()