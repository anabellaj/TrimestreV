def welcome():
    print('\n\t----WELCOME----\n')

def option(estudios):
    c = 1
    for k, v in estudios.items():
        for key, v in v.items():
            if key == 'Descripcion':
                print (f'Tipo de estudio: {k} - {v}')
                c += 1
    while True:
        opt = input('Please enter the letter corresponding to your study of choice:\n>> ').title()
        if opt not in ['U','T','R']:
            print('ERROR\nPlease remember the valid options are U, T or R')
            continue
        else:
            break
    study = estudios[opt]
    return study

def client_data(study):
    while True:
        try:
            cedula = int(input('Please enter your id:\n>> '))
            edad = int(input('Please enter your age:\n>> '))
            if edad not in range(0,101) or len(str(cedula)) > 8:
                print ('ERROR\nRemember that your id must only contain numbers and your age has to be between 0 and 100')
                continue
            else:
                break
        except:
            print ('ERROR\nRemember that your id must only contain numbers and your age has to be between 0 and 100')
    gender = input('Please enter your gender (M of F):\n>> ').title()
    while gender not in ['F', 'M']:
        gender = input('Please enter your gender (M of F):\n>> ').title()

    client = {
        'cedula': input('Please enter your id number\n> '),
        'edad': input('Please enter your age:\n> '),
        'gender' : input('Please enter your gender:\n> '),
        'study': study['Descripcion']
    }
    return client



def main():
    estudios = {
        'U':{'Descripcion': 'Ultrasonido', 'Precio': 45},
        'T':{'Descripcion':'Tomografia', 'Precio': 120},
        'R':{'Descripcion':'Resonancia', 'Precio': 150}
    }
    clients = []
    welcome()
    study = option(estudios)
    client = client_data(study)
    



main()