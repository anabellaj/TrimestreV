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
    clientes_con_descuento = 0
    descuento = 0
    study_key = client['study'][0]
    if client['gender'] == 'F' and client['edad'] > 55:
        descuento = estudios[study_key]['Precio'] *0.25
        clientes_con_descuento += 1
    elif client['gender'] =='M' and client['edad'] > 65:
        descuento = estudios[study_key]['Precio'] * 0.25
        clientes_con_descuento +=1
    precio = estudios[study_key]['Precio'] - descuento
    return precio

def factura(client, estudios, precio):
    study_key = client['study'][0]
    estudios[study_key]['Precio'] = precio
    print ('\n---------FACTURA---------')
    return (f"Cedula: {client['cedula']}\nEdad: {client['edad']}\nSexo: {client['gender']}\nTipo de estudio: {client['study']}\nMonto total: {estudios[study_key]['Precio']}")


def final_del_dia (total, u, r ,t, monto_facturado):
    print (f"\nEstadisticas del dia de hoy:\nClientes totales: {int(total)}\nClientes de ultrasonido: {int(u)}\nClientes de resonancia: {int(r)}\nClientes de tomografia: {int(t)}\n\nMonto total facturado: {monto_facturado}")

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
    monto_total = 0

    while True:
        welcome()
        print ('Por favor seleccione su tipo de estudio')
        study = option(estudios)
        client = client_data(study)
        clients.append(client)
        print (clients)
        precio = discount(client, estudios)
        monto_total += precio
        print (factura(client, estudios, precio))
        study_key = client['study'][0]
        if study_key == 'U':
            n_clientes += 1
            n_clientesU += 1.
        elif study_key == 'R':
            n_clientesR += 1
            n_clientes +=1
        elif study_key == 'T':
            n_clientesT += 1
            n_clientes += 1
        if input('Presione X para terminar el dia o cualquier tecla para continuar') == 'X':
            final_del_dia(n_clientes, n_clientesU,n_clientesR,n_clientesT, monto_total)
            break
main()