def correo():
    while True:
        try:
            correo = input('Por favor ingrese su correo electronico\n>> ')
            if len(correo) == 0 or len(correo) > 50:
                raise Exception
            correo_list= []
            for letter in correo:
                correo_list.append(letter)
                if not letter.isalnum() and letter != '.' and letter != '_' and letter != '@':
                    raise Exception
                if letter == ' ':
                    raise Exception
            if correo_list [0] == '@' or correo_list[0]== '/' or correo_list[0] == '.' or correo.count('@') != 1:
                raise Exception
            break
        except:
            print('Correo Electronico invalido\n Recuerde que no debe contener espacios, solo puede contener letras, numeros, "." y "_"\nEl correo solo puede contener 1 "@"\n')
    return correo    

def orden(shawarmas):
    orden = {}
    while True:
        print('Shawarmas disponibles:')
        while True:
            try:
                for k,v in shawarmas.items():
                    print (k, '- Precio:', v)
                type= input('\nIngrese el nombre del shawarma que desee: ').title()

                if type not in shawarmas.keys():
                    raise Exception
                break
            except:
                print('\nShawarma no disponible - Por favor ingrese el nombre de algun shawarma mostrado en pantalla\n')
        while True:
            try: 
                amount = int(input(f'Cuantos shawarmas desea del tipo {type}?\n>> '))
                break
            except:
                print('\nERROR - Por favor ingrese un numero entero\n')
        if type not in orden.keys():   
            orden.update({type: amount})
        else:
            orden [type] += amount
        if input('Presione X para pedir otro shawarma o cualquier tecla para finalizar su orden\n>> ').title() != 'X':
            break
    return orden
        
def descuento (amount):
    discount = False
    if amount % 2 != 0: 
        discount = True
    return discount
    
def precio_total(orden, shawarmas, discount):
    precio = 0
    for shawarma, cantidad  in orden.items():
        precio += shawarmas[shawarma] * cantidad
    if discount:
        precio -= precio*0.15
    return precio
    
def factura(order, precio, discount):
    while True:
        try:
            cedula = int(input('Por favor ingrese su cedula:\n>> '))
            break
        except:
            print('\nERROR - Recuerde que su cedula solo debe contener numeros')
    email = correo()
    print (f"\n\t------FACTURA------\nCedula: {cedula}\nCorreo: {email}\nMonto total: {precio}")
    for tipo, cantidad in order.items():
        print (f"Tipo de Shawarma: {tipo} - Cantidad: {cantidad}")
    if discount:
        print ('Descuento aplicado: Si')
    else:
        print('Descuento aplicado: No')
    client = {'cedula': cedula, 'email':email, 'orden':order, 'monto': precio, 'descuento': discount}
    return client

def amount(clients):
    total = 0
    tipo_mix = 0
    tipo_trad = 0
    tipo_saman = 0
    for client in clients:
        for k,v in client.items():
            if k =='orden':
                for tipo, cantidad in v.items():
                    if tipo == 'Tradicional': tipo_trad += cantidad
                    elif tipo == 'Mixto': tipo_mix+=cantidad
                    elif tipo == 'Saman': tipo_saman+=cantidad
                    total += cantidad
    if total == 0:
        print('No se han vendido shawarmas el dia de hoy')
    print (f'CANTIDAD DE SHAWARMAS VENDIDOS POR TIPO\nTradicional: {tipo_trad} shawarmas\nMixto: {tipo_mix} shawarmas\nSaman: {tipo_saman} shawarmas')
    print ('Total de shawarmas vendidos en el dia:',total, 'shawarmas')

def clientes_descuento(clientes):
    total_descuento = 0
    for cliente in clientes:
        if cliente['descuento']:
            total_descuento += 1
    return total_descuento

def kibbes (client):
    kibbes = False
    for k,v in client.items():
        if k =='orden':
            for tipo, cantidad in v.items():
                if tipo == 'Saman':
                    kibbes = 2*cantidad
    return kibbes
                  

def main():
    shawarmas = {
        'Tradicional': 8,
        'Mixto':12,
        'Saman': 15
        }
    correos = []
    clients = []
    contador = 1
    while True:    
        cantidad = {}
        total_descuento = 0
        while True:
            try:
                run = int(input('\n------BIENVENIDO A SAMAN SHAWARMAS-------\nPresione 1 para comprar\nPresione 2 para ver la cantidad de shawarmas vendidos por cada tipo\nPresione 3 para ver la cantidad de clientes con descuento\nPresione 4 para elegir el ganador del concurso\nPresione 5 para salir\n\n>> '))
                if run not in range (1,6):
                    raise Exception
                break
            except:
                print('\nERROR - Opcion Invalida')
        if run == 1:
            # Cantidad: Dict con [shawarmas,cantidad]
            cantidad = (orden(shawarmas))
            suma_cantidad = 0
            for v in cantidad.values():
                suma_cantidad += v
            print(f'\nSu orden tiene un total de {suma_cantidad} shawarmas\nORDEN #{contador}')
            for tipo, cant in cantidad.items():
                print (tipo, '-', cant, 'shawarmas')
            if input(f'\nPresione X para salir o cualquier tecla para finalizar su orden\n>> ').title() == 'X':
                continue
            discount = descuento(suma_cantidad)
            price = precio_total(cantidad, shawarmas, discount)
            client = factura(cantidad, price, discount)
            clients.append(client)
            kibbe = kibbes(client)
            if kibbe: 
                print ('SHAWARMA SAMAN SELECCIONADO\nCantidad de kibbes a preparar:', kibbe)
            correos.append(client['email'])
            contador += 1
            kibbe = False
        elif run == 2:
            # Numero de shawarmas por tipo
            amount(clients)
        elif run == 3:
            # Numero de clientes con descuento
            total_descuento = clientes_descuento(clients)
            print('Total de clientes con descuento aplicado:', total_descuento)
        elif run ==4:
            max = ''
            for correo in correos:
                if len(correo)>len(max):
                    max = correo
            print(f'\nEl correo ganador es {max}. Felicidades!')
        elif run == 5:
            print('Hasta pronto! Esperamos haya disfrutado su visita el dia de hoy.')
            break
                        
        
main()