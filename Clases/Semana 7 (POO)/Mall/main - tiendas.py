from ClaseTiendas import Tiendas

tipos = ["Women's Apparel", "Men's Apparel", "Children's Apparel", "Footwear", "Health & Beauty", "Jewelry & Watches", "Sporting Goods & Apparel", "Luggage & Handbags", "Optical/Eyewear","Electronics","Food", "Entertainment & Attractions", "Toys & Hobbies", "Home Décor", "Department Store", "Services", "Other"]
pisos = ['PB','P1','P2','P3']

def get_opt ():
    while True:
        try:
            opt=int(input('What do you wish to do today?\n1. Register a store\n2. See all registered stores\n3. Exit\n>> '))
            if opt not in range(1,4):
                raise Exception
            break
        except:
            print('\nERROR - Please enter a valid option')
    return opt 

def registrar_tienda(tiendas):
    nombre = input('Please enter the name of the store:\n>> ').title()
    while nombre in tiendas:
        nombre = input('That store is already registered\nPlease enter the name of the new store:\n>> ')
    for i,t in enumerate(tipos):
        print(f'{i+1}. {t}')
    while True:
        try:
            tipo = int(input('Enter the number corresponding to the store type:\n>> '))
            if tipo not in range(len(tipos)):
                raise Exception
            break
        except:
            print('\nERROR - Please enter a valid option')
    for i,t in enumerate(tipos):
        if tipo == i+1:
            tipo = t
    for i,p in enumerate(pisos):
        print(f'{i}. {p}')
    while True:
        try:
            piso = int(input('Enter the number corresponding to the store floor:\n>> '))
            if piso not in range(len(pisos)+1):
                raise Exception
            break
        except:
            print('\nERROR - Please enter a valid option')
    for i,p in enumerate(pisos):
        if piso == i:
            piso = p
    rif = input('Please enter the store RIF:\n>> ').upper()
    owner = input('Please enter the full name of the store owner\n>> ').title()
    while True:
        try:
            owner_phone = int(input('Please enter the phone of the store owner:\n>> '))
            if len(str(owner_phone)) not in range(10,12):
                raise Exception
            break
        except:
            print('\nERROR - Remember to enter a complete phone numbers, without special characters or letters') 
    
    nueva_tienda = Tiendas(nombre,tipo,piso,rif,owner,owner_phone)
    tiendas.append(nueva_tienda)
    return tiendas

def get_filter():
    while True:
        try:
            filter = int(input('By which characteristic do you wish to order the stores?\n1. By name\n2. By floor\n3. By type\n>> '))
            if filter not in range(1,4):
                raise Exception
            break
        except:
            print('ERROR - Please enter a valid option')
    return filter

def see_stores(tiendas):
    filter = get_filter()
    if filter == 1:
        tiendas.sort(key = lambda tienda: tienda.nombre)
    elif filter == 2:
        tiendas.sort(key = lambda tienda:tienda.piso)
    elif filter == 3:
        tiendas.sort(key = lambda tienda:tienda.tipo)
        
    for i,t in enumerate(tiendas):
        print('---------------TIENDA',i+1,'-------------')
        t.mostrar()
        
            
def main():
    print('\nWelcome to the mall!\n')
    tiendas = []
    while True:
        opt = get_opt()
        if opt == 1:
            registrar_tienda(tiendas)
        elif opt == 2:
            if len(tiendas) == 0:
                print('No stotres have been registered yet.')
            else:
                see_stores(tiendas)
        elif opt == 3:
            print('\nSee you soon!\n')
            break
main()