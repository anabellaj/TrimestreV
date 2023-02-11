def welcome():
    print('\n\t----BIENVENIDO----\n')

def option(estudios):
    c = 1
    for k, v in estudios.items():
        for key, v in v.items():
            if key == 'Descripcion':
                print (f'Tipo de estudio: {k} - {v}')
                c += 1
    while True:
        opt = input('Por favor ingrese la letra correspondiente:\n>> ').title()
        if opt not in ['U','T','R']:
            print('ERROR\nRecuerde que las opciones validas son U, T o R')
            continue
        else:
            break
    study = estudios[opt]
    return study

def client_data(study):
    while True:
        try:
            cedula = int(input('Por favor ingrese su cedula:\n>> '))
            edad = int(input('Por favor ingrese su edad:\n>> '))
            if edad not in range(0,101) or len(str(cedula)) > 8:
                print ('ERROR\nRecuerde que su id solo debe contener numeros y su edad debe estar entre 0 y 101')
                continue
            else:
                break
        except:
            print ('ERROR\nRecuerde que su id solo debe contener numeros y su edad debe estar entre 0 y 10')
    gender = input('Por favor ingrese su sexo (M of F):\n>> ').title()
    while gender not in ['F', 'M']:
        gender = input('\nERROR\nPor favor ingrese su sexo (M of F):\n>> ').title()

    client = {
        'cedula': cedula,
        'edad': edad,
        'gender' : gender,
        'study': study['Descripcion']
    }
    return client

def discount (client, estudios):
    descuento = 0
    study_key = client['study'][0]
    if client['gender'] == 'F' and client['edad'] > 55:
        descuento += estudios[study_key]['Precio'] *0.25
    elif client['gender'] =='M' and client['edad'] > 65:
        descuento += estudios[study_key]['Precio'] * 0.25
    return descuento

def monto_final(client, descuento, estudios):
    precio = 0
    study_key = client['study'][0]
    precio += estudios[study_key]['Precio'] - descuento
    return precio

def factura(client, estudios, precio):
    print ('\n---------FACTURA---------')
    return (f"Cedula: {client['cedula']}\nEdad: {client['edad']}\nSexo: {client['gender']}\nTipo de estudio: {client['study']}\nMonto total: {precio}")


def final_del_dia (total, u, r ,t, descuentos, monto_facturado):
    print (f"\nEstadisticas del dia de hoy:\nClientes totales: {int(total)}\nClientes de ultrasonido: {int(u)}\nClientes de resonancia: {int(r)}\nClientes de tomografia: {int(t)}\n\nTotal de clientes con descuento: {int(descuentos)}\nMonto total facturado: {monto_facturado}")

def main():

    estudios = {
        'U':{'Descripcion': 'Ultrasonido', 'Precio': 45},
        'T':{'Descripcion':'Tomografia', 'Precio': 120},
        'R':{'Descripcion':'Resonancia', 'Precio': 150}
    }
    clients = []
    n_clientes = 0
    n_clientesU = 0
    n_clientesR = 0
    n_clientesT = 0
    clientes_descuento = 0
    dinero = 0

    while True:
        welcome()
        print ('Por favor seleccione su tipo de estudio')
        study = option(estudios)
        client = client_data(study)
        clients.append(client)
        descuento = discount(client, estudios)
        monto_total = monto_final(client, descuento,estudios)
        dinero += monto_total
        print (factura(client, estudios, monto_total))
        study_key = client['study'][0]
        if monto_total != estudios[study_key]['Precio']:
            clientes_descuento += 1
        if study_key == 'U':
            n_clientes += 1
            n_clientesU += 1.
        elif study_key == 'R':
            n_clientesR += 1
            n_clientes +=1
        elif study_key == 'T':
            n_clientesT += 1
            n_clientes += 1
        if input('Presione X para terminar el dia o cualquier tecla para continuar\n>> ').title() == 'X' :
            final_del_dia(n_clientes, n_clientesU,n_clientesR,n_clientesT, clientes_descuento, dinero)
            break
main()