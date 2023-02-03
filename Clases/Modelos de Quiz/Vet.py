doctors = ['Angela Johnson', 'David Kane', 'Marcus Stewart', 'Jessica Cruz']
services = [
    {
        "name": "Consulta",
        "price": 20,
    },
    {
        "name": "Operación",
        "price": 80,
    },
    {
        "name": "Peluquería",
        "price": 30,
    },
]
pets = {}
pet_types = ["Perro", "Gato", "Pájaro"]
payments = []
vowels = ['a', 'e', 'i', 'o', 'u']

# Seleccionar doctor que utiliza el programa
while True:
    print ('Welcome!')
    opt = input('Press:\n1 Register a pet\n2 ')
    contador = 1
    for doctor in doctors:
        print (contador, doctor)
        contador += 1
    name_number = input ('Please enter the number corresponding to you name:\n>>')
    while name_number not in ['1','2','3','4']:
        name = input ('Please enter the number corresponding to you name:\n>>')
    name_number = int(name_number)
    print (f'Welcome {doctors[name_number-1]}!')
    


