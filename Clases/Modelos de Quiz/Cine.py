# Vender entradas a la funcion
# Precios: Lunes y Martes = 2, Miercoles a Domingo = 5
precios = {'General': 5, 'Rebaja': 2}
horas = {1: '12:00pm',2: '2:30pm',3:'4:00pm',4:'6:00pm'}
dias = {'LU':'Lunes','MA':'Martes','MI':'Miercoles','JU':'Jueves','VI':'Viernes','SA':'Sabado','DO':'Domingo'}
rebaja = False
run = input('\nBienvenido al cine! \nPulsa x para comprar una entrada o cualquier tecla para salir.\n>> ')
while run == 'x':
    name = input ('\nPor favor ingrese su nombre completo:\n>> ')
    cedula = input('\nPor favor ingrese su numero de cedula (sin puntos!):\n>> ')
    while not cedula.isnumeric():
        cedula = input('\nIngreso Invalido\nPor favor ingrese su numero de cedula (sin puntos!):\n>> ')
    fila_asiento = input('\nPor favor ingrese su fila de asiento:\n>>').title()
    while len(fila_asiento ) != 1 or not fila_asiento.isalpha():
        fila_asiento = input('\nIngreso Invalido\nPor favor ingrese su fila de asiento:\n>> ').title()
    numero_asiento = input('\nPor favor ingrese su numero de asiento:\n>> ')
    while not numero_asiento.isnumeric() or len(str(numero_asiento)) > 2:
        numero_asiento = input('\nIngreso Invalido\nPor favor ingrese su numero de asiento:\n>> ')
    dia = input('\nIngrese el dia de su funcion\nLU - Lunes\nMA - Martes\nMI - Miercoles\nJU - Jueves\nVI - Viernes\nSA - Sabado\nDO - Domingo\nIngrese las letras correspondientes a su dia >> ').upper()
    while dia not in ['LU','MA','MI','JU','VI','SA','DO']:
        dia = input('\nIngreso Invalido\nIngrese el dia de su funcion\nLU - Lunes\nMA - Martes\nMI - Miercoles\nJU - Jueves\nVI - Viernes\nSA - Sabado\nDO - Domingo\nIngrese las letras correspondientes a su dia >> ').upper()
    if dia == 'LU' or dia == 'MA':
        coste = precios['Rebaja']
        rebaja = True
    elif dia != 'LU' or dia !='MA':
        coste =precios ['General']
    hora = input ('\nElija la hora de su funcion\n1. 12:00m\n2. 2:30pm\n3. 4:00pm\n4. 6:00pm\nIngrese el numero correspondiente a la hora de su eleccion >> ')
    while hora not in ['1','2','3','4']:
        hora = input ('\nIngreso Invalido\nElija la hora de su funcion\n1. 12:00m\n2. 2:30pm\n3. 4:00pm\n4. 6:00pm\nIngrese el numero correspondiente a la hora de su eleccion >> ')
    hora = int (hora)
    while True:
        email = input('\nIngrese su correo electronico para participar en una rifa\n>>')
        if len(email) == 0 or len(email) > 50:
            print ('\n\t---------------------ERROR---------------------\n>> Su correo debe tener entre 1 y 50 caracteres.\n Por favor intente de nuevo')
            continue
        email_list = []
        for letter in email:
            if letter == '' or (not letter.isalnum() and not letter in ['@','.','_']):
                print ('\n\t---------------------ERROR---------------------\nSu correo no puede contener espacios y solo se permiten letras, numeros, puntos o guiones. Recuerde que debe contener un @.')
                continue
            else:
                email_list.append(letter)
        if email_list [0] == '@' or email_list[0]== '/' or email_list[0] == '.':
            print ('\n\t---------------------ERROR---------------------\nSu correo no puede empezar con @, . o /.\nPor favor intente de nuevo.')
            continue
        if email_list.count('@') != 1:
            print ('\n\t---------------------ERROR---------------------\nSU correo solo debe contener 1 "@".\nPor favor intente de nuevo. ')
        else:
            break
    print ('\n\t------------------RECIBO------------------\nNombre:',name,'\nCedula:',cedula,'\nEmail:',email,'\nAsiento:',fila_asiento+numero_asiento,'\nDia y hora:', dias[dia] + horas[int(hora)], 'Precio',)

