from Alcohol import Alcohol
from Refresco import Refresco
from Bebida import Bebida

def actualizar_almacen(almacen_desactualizado):
    almacen = []
    for clase, bebidas in almacen_desactualizado.items():
        for bebida in bebidas:
            if clase == 'Alcohol':
                x = Alcohol(bebida['nombre'],bebida['marca'],bebida['disponible'],bebida['grado'],bebida['tipo'])
                almacen.append(x)
            elif clase == 'Refresco':
                x = Refresco(bebida['nombre'],bebida['marca'],bebida['disponible'],bebida['azucar'],bebida['sabor'])
                almacen.append(x)
    return almacen

def ver_inventario (almacen):
    for num, item in enumerate(almacen):
        if isinstance(item, Alcohol):
            print('--------',{num+1},'----------')
            print('BEBIDA ALCOHOLICA')
            item.mostrar()
        if isinstance(item, Refresco):
            print('--------',{num+1},'----------')
            print('REFRESCO')
            item.mostrar()

def eliminar(almacen):
    ver_inventario(almacen)
    while True:
        try: 
            indice = int(input('Indique el numero de la bebida a eliminar\n>> '))
            if indice not in range(1,len(almacen)+1):
                raise Exception
            break
        except:
            print(f"ERROR - Recuerde solo ingresar numeros y que solo hay {len(almacen)} bebidas en total")
    indice = indice -1
    for n, item in enumerate(almacen):
        if n == indice:
            item.disponible = False
            print('\nBebida eliminada')
    return almacen   

def mayor_grado(almacen):
    max, max_item = 0,0
    for item in almacen:
        if isinstance(item, Alcohol):
            if item.grado > max:
                max = item.grado
                max_item = item.nombre
    return max_item, max

def min_azucar(almacen):
    min, min_item = 100,0
    for item in almacen:
        if isinstance(item, Refresco):
            if item.azucar < min:
                min = item.azucar
                min_item = item.nombre
    return min_item, min

def marcas_2cat (almacen):
    soda_brands, alcohol_brands= [], []
    for bebidas in almacen:
        if isinstance(bebidas, Refresco):
            soda_brands.append(bebidas.marca)
        elif isinstance(bebidas, Alcohol):
            alcohol_brands.append(bebidas.marca)
    both = []
    for brands in soda_brands:
        for brand in alcohol_brands:
            if brands == brand:
                both.append(brand)
    return both

def main():
    almacen_desactualizado = {
        "Alcohol":
        [
        { "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True },
        { "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky",
        "disponible": True },
        { "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible": True }
        ],
        "Refresco":
        [
        { "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible": True },
        { "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
        { "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon",
        "disponible": True }]}
    almacen = actualizar_almacen(almacen_desactualizado)
    
    while True:
        print('\nBIENVENIDO AL BODEGON\n')
        while True:
            try:
                opt = int(input('Presione 1 para ver el inventario\nPresione 2 para eliminar bebidas\nPresione 3 para ver las estadisticas\nPresione 4 para salir\n\n>>'))
                if opt not in range(1,5):
                    raise Exception
                break
            except:
                print('ERROR - Por favor ingrese una opcion valida')
            
        # 1: Ver inventario
        if opt == 1:
            print('\n--------------INVENTARIO---------------\n')
            ver_inventario(almacen)
        
        # 2: Eliminar bebida
        elif opt == 2:
            almacen = eliminar(almacen)
        
        # 3: Mostrar estadisticas
        elif opt == 3:
            print('\n----------ESTADISTICAS----------')
            nombre, grade = mayor_grado(almacen)
            name, porcentaje = min_azucar(almacen)
            marcas = marcas_2cat(almacen)
            print(f"La bebida con el mayor grado de alcohol es {nombre}, la cual tiene un grado de {grade}°\nLa bebida con el menor porcentaje (%) de azucar es {name}, el cual es de {porcentaje}%")
            print('Las marcas que tienen tanto bebidas alcoholicas como refrescos son:', end =' ')
            for brand in marcas:
                print(brand, end='')
            print('.\n')
        # 4: Salir
        else:
            print('\nHasta pronto\n')
            break                    
    
main()