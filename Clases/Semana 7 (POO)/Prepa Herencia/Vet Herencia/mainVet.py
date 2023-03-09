# Sistema de facturacion de un veterinario
# Los animales disponibles son: loros, gatos, perros, hamsters
# Cada factura debe tener los atributos de cada clase

from Animal import Animal
from Perro import Perro
from Gato import Gato
from Loro import Loro
from Hamster import Hamster

def generar_factura(ani):
    nombre = input('Por favor ingrese el nombre del animal: ').title()
    while True:
        try:
            edad = int(input('Por favor ingrese la edad del animal: '))
            break
        except:
            print('\nERROR - Por favor ingrese una opcion valida')
    raza = input('Ingrese la raza: ').title()
    owner = input('Ingrese el nombre del propietario: ').title()
    owner_phone = input('Ingrese el numero de telefono del propietario: ')
    sexo = input('Ingrese el sexo del animal: ').title()
    vacunas = input('El animal ha sido vacunado? ').title()
    x = ''
    # Perro
    if ani == 1:
        pelaje = input('Ingrese el estado del pelaje: ').title()
        x = Perro(nombre, edad, sexo, raza, vacunas, owner, owner_phone, pelaje)
    # Gato
    elif ani == 2:
        pelaje = input('Ingrese el estado del pelaje: ').title()
        estado_bigotes =  input('Ingrese el estado de los bigotes: ').title()
        cut_nails = input('Se le han cortado las unas al animal? ').title()
        x = Gato (nombre, edad, sexo, raza, vacunas, owner, owner_phone, pelaje, estado_bigotes, cut_nails)
    # Loro
    elif ani == 3:
        plumaje = input('Ingrese el estado del plumaje: ').title()
        alas = input('Ingrese el estado de las alas: ').title()
        x = Loro (nombre, edad, sexo, raza, vacunas, owner, owner_phone, plumaje, alas)
    # Hamster
    elif ani == 4:
        pelaje = input('Ingrese el estado del pelaje: ').title()
        dientes = input('Ingrese el estado de los dientes: ').title()
        x = Hamster(nombre, edad, sexo, raza, vacunas, owner,owner_phone,pelaje,dientes)
    return x     
    
def buscar_factura(facturas, fact):
    for k,v in facturas.items():
        if k == fact:
            v.mostrar()

def eliminar_factura(facturas, factx):
    for k,v in facturas.items():
        if k == factx:
            facturas.pop(k)
    return facturas
            
def modificar_factura(facturas, factm):
    for k,v in facturas.items():
        if k == factm:
            param = input('Ingrese el numero nuevo de telefono:\n>> ')
            facturas[k].owner_phone = param
            return facturas

def main():
    facturas = {}
    while True:
        print('\nBienvenido al veterinario!\n')
        while True:
            try:
                opt=int(input('Que desea relizar hoy?\n1. Agregar factura\n2. Imprimir todas las facturas\n3. Buscar factura\n4. Eliminar factura\n5. Modificar factura\n6. Salir\n>> '))
                if opt not in range (1,7):
                    raise Exception
                break
            except:
                print('\nERROR - Por favor ingrese una opcion valida')
                
        # Agregar factura
        if opt ==1:
            while True:
                try:
                    ani=int(input('Seleccione el tipo de animal\n1. Perro\n2. Gato\n3. Loro\n4. Hamster\n>> '))
                    if ani not in range (1,5):
                        raise Exception
                    break
                except:
                    print('\nERROR - Por favor ingrese una opcion valida')
            facturas[len(facturas)+1] = generar_factura(ani)
            pass
        
        #Imprimir facturas
        elif opt ==2:
            print('Las facturas registradas son:')
            for k,v in facturas.items():
                print(f"---------Factura {k}----------\n{v.mostrar()}")
        
        #Buscar facturas 
        elif opt ==3:
            while True:
                try:
                    fact = int(input('Ingrese el numero de la factura a buscar:\n>> '))
                    if fact > len(facturas):
                        print(f'La factura numero {fact} no esta disponible')
                        break
                    break
                except:
                    print('\nERROR - Por favor solo ingrese numeros enteros')
            buscar_factura(facturas, fact)
        
        #Eliminar facturas:
        elif opt ==4:
            while True:
                try:
                    factx = int(input('Ingrese el numero de la factura a eliminar:\n>> '))
                    if factx > len(facturas):
                        print(f'La factura numero {factx} no esta disponible')
                        break
                    break
                except:
                    print('\nERROR - Por favor solo ingrese numeros enteros')
            facturas = eliminar_factura(facturas, factx)
        
        # Modificar factura
        elif opt == 5:
            while True:
                    try:
                        factm = int(input('Ingrese el numero de la factura a eliminar:\n>> '))
                        if factm > len(facturas):
                            print(f'La factura numero {factm} no esta disponible')
                            break
                        break
                    except:
                        print('\nERROR - Por favor solo ingrese numeros enteros')
            facturas = modificar_factura(facturas, factm)
            
        #Salir
        else:
            
            print('\nHasta pronto!\n')
            break
    
main()