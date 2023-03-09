from Vehiculo import Vehiculo
from Automovil import Automovil
from Motocicleta import Motocicleta

vehiculos = [ 
    { "tipo": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "tipo": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "tipo": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"},
]


def registrar_vehiculo():
    tipo = int(input('Ingrese su tipo de vehiculo\n1. Automovil\n2. Motocicleta\n>> '))
    
    placa = input('Ingrese placa: ')
    marca = input('Ingrese marca: ')
    puesto = input('Ingrese puesto: ')
    hora_entrada = input('Ingrese hora de entrada: ')
    hora_salida = ''
    x = ''
    if tipo ==2:
        tipo = 'Moto'
        x = Motocicleta(tipo,placa,marca,puesto,hora_entrada,hora_salida)
        
    elif tipo ==1:
        tipo = 'Automovil'
        minusvalido = input('Es usted minusvalido? ')
        x = Automovil(tipo, placa, marca, puesto, hora_entrada, hora_salida, minusvalido)
        
    return x 

def salida(nueva_db):
    i = 0
    for x in nueva_db:
        if x.hora_salida== '':
            i+=1
            print('--------',{i},'----------')
            x.mostrar()
    select = int(input('Seleccione el carro que va a salir: '))
    hora = input('Ingrese la hora de salida ')
    
    nueva_db[select-1].hora_salida = hora
    return nueva_db

def main():
    nueva_db = []
    while True:
        opt = int(input('BIENVENIDO\nQue desea realizar hoy?\n1. Registro\n2. Salida\n3. Ver vehiculos estacionados actualmente\n4. Salir\n>> '))
        if opt == 1:
            x= registrar_vehiculo()
            nueva_db.append(x)
        elif opt ==2:
            nueva_db = salida(nueva_db)
            
        elif opt ==3:
            i = 0
            for x in nueva_db:
                if x.hora_salida== '':
                    i+=1
                    print('--------',{i},'----------')
                    x.mostrar()
            
        elif opt ==4:
            print('Hasta pronto!')
            break
            
    
main()