# Conseguir hipotenusa teniendo dos catetos
while True:
    op = input('Ingrese el valor del cateto opuesto: ')
    ad = input('Ingrese el valor del cateto adyacente: ')
    if not op.isnumeric() or not ad.isnumeric():
        print('\nRecuerde ingresar numeros')
        continue
    else:
        op = int(op)
        ad = int(ad)
    break

mult = (op**2) + (ad**2)
hipotenusa = mult**0.5
print (f'La hipotenusa es {hipotenusa}.')