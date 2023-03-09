from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Microondas import Microondas
from Nevera import Nevera
from Licuadora import Licuadora

def get_productos (diccionario):
    productos = []
    for v in diccionario['washer']:
        x = Lavadora(v['cod_p'],v['price'],v['brand'],v['color'],v['capacity'])
        productos.append(x)
    for v in diccionario['microwave']:
        x = Microondas(v['cod_p'],v['price'],v['brand'],v['color'],v['digital'])
        productos.append(x)
    for v in diccionario['fridge']:
        x = Nevera(v['cod_p'],v['price'],v['brand'],v['color'],v['cooler'],v['comp'])
        productos.append(x)
    for v in diccionario['blender']:
        x = Licuadora(v['cod_p'],v['price'],v['brand'],v['color'],v['cup'],v['speeds'])
        productos.append(x)
    return productos

def inventario (productos):
    for num, item in enumerate(productos):
        if isinstance(item, Lavadora):
            print('--------',{num+1},'----------')
            print('- LAVADORA -')
            item.mostrar()
        if isinstance(item, Microondas):
            print('--------',{num+1},'----------')
            print('- MICROONDAS -')
            item.mostrar()
        if isinstance(item, Nevera):
            print('--------',{num+1},'----------')
            print('- NEVERA -')
            item.mostrar()
        if isinstance(item, Licuadora):
            print('--------',{num+1},'----------')
            print('- LICUADORA -')
            item.mostrar()
            
def eliminar (productos, eliminados):
    inventario(productos)     
    while True:
        try: 
            indice = int(input('Indique el numero del producto a eliminar\n>> '))
            if indice not in range(1,len(productos)+1):
                raise Exception
            break
        except:
            print(f"ERROR - Recuerde solo ingresar numeros y que solo hay {len(productos)} productos en total")
    indice = indice -1
    for n, item in enumerate(productos):
        if n == indice:
            productos.remove(item)
            eliminados.append(item)
            print('\nProducto eliminado')
    return productos, eliminados 
    
def mayor_precio(productos):
    max_precio, max_item = 0,0
    for item in productos:
        if item.precio > max_precio:
            max_precio = item.precio
            max_item = item.codigo_producto
    return max_item, max_precio  
    
def main():
    edd = {
    "washer":
    [
        {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
        {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
    ],
    "microwave":
    [
        {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
        {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
    ],
    "fridge":
    [
        {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
        {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
    ],
    "blender":
    [
        {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
        {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
    ]
    }
    eliminados = []
    productos = get_productos(edd)
    while True:
        print('BIENVENIDO A LA TIENDA DE ELECTRODOMESTICOS!')
        while True:
            try:
                opt = int(input('\nPresione 1 para ver el inventario\nPresione 2 para eliminar un producto\nPresione 3 para ver las estadisticas\nPresione 4 para salir\n\nIngrese la opcion a seleccionar\n>> '))
                if opt not in range(1,5):
                    raise Exception
                break
            except:
                print('ERROR - Recuerde ingresar una opcion valida por favor!')
        # 1: Mostrar inventario     
        if opt == 1:  
            inventario(productos)
        # 2: Eliminar producto
        elif opt == 2:
            productos, eliminados = eliminar(productos, eliminados)
        # 3: Ver estadisticas
        elif opt == 3:
            print('\n-------ESTADISTICAS-------\n')
            print('\tProductos eliminados:')
            for i, producto in enumerate(eliminados):
                print(f"\t---{i+1}---")
                producto.mostrar()
            max_item, max_price = mayor_precio(productos)
            print(f"\tEl producto de mayor precio es {max_item} el cual tiene un precio de {max_price}$\n\n\tNeveras disponibles: ")
            i = 1
            for product in productos:
                if isinstance(product, Nevera):
                    print('---',i,'---')
                    product.mostrar()
                    i += 1     
        # 4: Salir
        elif opt ==4:
            print('\nHasta pronto!')
            break

main()