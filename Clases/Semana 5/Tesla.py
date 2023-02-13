def choose_car(cars):
    choose_car = ''
    while True:
        try: 
            for k,v in cars.items():
                print (f'Car model: {k} - Price: {v}')
            choose_car = input('\nPlease enter the name of the model you wish to purchase:\n>> ').title()
            if choose_car not in cars.keys():
                raise Exception
            else:
                break
        except:
            print("\nWe're sorry, that car is not available\nPlease choose a model from the following list:")
    return choose_car

def client (choice):
    while True:
        try: 
            email = input('Please enter your complete email address\nRemember that it must contain one "@"\n>> ')
            if email.count('@') != 1:
                raise Exception
            break
        except:
            print('\nInvalid email address\n')
    while True:
        try:
            age = int(input('Please enter your age:\n>> '))
            if age not in range (18,101):
                raise Exception
            break
        except:
            print('\nRemember to only enter integer numbers\nYou must be between 18 and 100 years old to purchase a car')
    autopilot = input('Do you wish for your car to have AutoPilot?\nEnter "yes" or "no"\n>> ').upper()
    while autopilot not in ['YES', 'NO']:
        autopilot = input('\nERROR - Invalid Option\nDo you wish for your car to have AutoPilot?\nEnter "yes" or "no"\n>> ').upper()
    if autopilot == 'YES':
        autopilot = True
    else:
        autopilot = False
    client = {'Email Address': email,
               'Age': age,
               'Model': choice,
               'AutoPilot': autopilot,
               'Price': ''}
    
    return client
    
def factura (cars, client, choice):
    price = cars[choice]
    if client['AutoPilot']:
        price = (cars[choice] *0.05) + cars[choice]
    client['Price']= price
    print(f"\n----------RECEIPT---------")
    for k, v in client.items():
        print(k, '->', v)
    return client
  
def filter (cars, facturas):
    while True:
        try:
            filter = input("Which car model's receipt do you wish to see?\nRemember the car models available are S, 3, X, Y and Cybertruck\nEnter the name of the model\n>> ").title()
            if filter not in cars.keys():
                raise Exception
            break
        except:
            print('ERROR - Invalid option')
    print(f'\nRECEIPTS OF MODEL {filter}')
    find = False
    for factura in facturas:
        if factura ['Model'] == filter:            
            for k,v in  factura.items():
                print (k, '->', v)
                find = True
    if find == False:
        print(f'There are no receipts corresponding to the model {filter}')
                
def average(facturas):
    averageX = 0
    averageS = 0
    average3 = 0
    averageY =0
    averageCyber =0
    for facturas in facturas:
        if facturas['Model'] == 'X':
            averageX +=1
        elif facturas['Model'] == 'S':
            averageS += 1
        elif facturas['Model'] == '3':
            average3 += 1
        elif facturas['Model'] == 'Y':
            averageY+= 1
        elif facturas['Model'] =='Cybertruck':
            averageCyber+= 1
    print(f'\nTOTAL CARS SOLD FOR EACH MODEL\nModel X: {averageX}\nModel S: {averageS}\nModel 3: {average3}\nModel Y: {averageY}\nModel Cybertruck: {averageCyber}')
    
def main():
    cars = {
        'S': 30000,
        '3': 40000,
        'X': 50000,
        'Y': 70000,
        'Cybertruck': 90000
    }    
    facturas = []
    while True:
        print('\n\t-------------------WELCOME TO TESLA-------------------')
        while True:
            try:
                run = int(input('Press 1 to purchase a car\nPress 2 to filter receipts\nPress 3 to see the number of cars bought for each model\nPress 4 to show all receipts from higher to lower price\nPress 5 to exit\n>> '))
                if run  not in range (1,6):
                    raise Exception
                break
            except:
                print('\nERROR - Invalid Option\n')
        if run == 1:
            choice = choose_car(cars)
            cliente = client(choice)
            precios = factura(cars,cliente,choice)
            facturas.append(precios)
        elif run == 2:
            filter (cars,facturas)
        elif run == 3:
              average(facturas)
        elif run == 4:
            # Ordenar una lista de diccionarios a partir de un value de cada diccionario
            facturas.sort(key = lambda p:p ['Price'], reverse=True)
            print(facturas)
        elif run == 5:
            print('Hasta pronto!')
            break      
main()