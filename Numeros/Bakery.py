def menus(menu):
    print('\t-------------MENU------------')
    for k,v in menu.items():
        print (f'{k} - Precio: {v}$')

def orden(menu):
    orden = {}
    while True:
        menus(menu)
        producto= input('\nIngrese el nombre del producto a comprar:\n>> ').title()
        while producto not in menu.keys():
            producto= input('\nERROR - Producto no disponible\nIngrese el nombre del producto a comprar:\n>> ').title()
        amount = input(f'Cuandos productos de tipo {producto} desea?\n>> ')
        while not amount.isnumeric():
            amount = input(f'\nERROR - Por favor solo ingrese numeros enteros\nCuandos productos de tipo {producto} desea?\n>> ')
        amount=int(amount)
        orden.update({producto: amount})
        if input('Presione X para ordenar otro producto o cualquier tecla para finalizar su orden\n>> ').title() != 'X':
            break
    nombre = input('Por favor ingrese su nombre\n>> ').title()
    cedula = input('Por favor ingrese su cedula:\n>> ')
    while not cedula.isnumeric():
        cedula = input('\nERROR - Solo ingrese numeros (no puntos!)\nPor favor ingrese su cedula:\n>> ')
    precio = 0
    for product,amount in orden.items():
        precio += menu[product] * amount
    cliente = {'nombre': nombre, 'cedula': cedula, 'orden': orden, 'monto': precio}
    return cliente
    
    
def main():
    menu = {"Cachito": 4.00, "Empanada": 3.00, "Pasatelito": 3.50, "Sandwich": 2.50, "Pan tradicional (1 barra)": 1.00, "Pan especial (1 barra)": 1.75, "Café": 1.25, "Jugo": 2.00, "Agua": 0.75, "Dulces (por kilo)": 6.00, "Galletas (por kilo)": 5.75, "Torta": 10.25}
    while True:
        input('Bienvenido a la Panaderia\nPresione cualquier tecla para realizar su compra ')
        print(orden(menu))
main()
