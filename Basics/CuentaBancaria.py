# Imprimir cada operacion realizada

saldo = 3480
fecha = '10/04/2020'
print (f'Para la fecha {fecha} el saldo es de {saldo}$.\n')

# 11/04/2020 tienda de ropa, gasto 96$
gasto = 96
saldo -= gasto
fecha = '11/04/2020'
print (f'Se gastaron {gasto}$.')
print (f'Para la fecha {fecha} el saldo es de {saldo}$.\n')

# 17/04/2020 se cobra 1200$
sueldo = 1200
saldo += sueldo
fecha = '17/04/2020'
print (f'Se cobro un sueldo de {sueldo}$.')
print (f'Para la fecha {fecha} el saldo es de {saldo}$.\n')

# 30/04/2020 se cobra 3% de interes
interes = saldo*0.03
saldo += interes
fecha = '30/04/2020'
print (f'Se cobro un interes de {interes}$.')
print (f'Para la fecha {fecha} el saldo es de {saldo}$.\n')

# 02/05/2020 supermercado, gasto 51$
gasto = 51
saldo -= gasto
fecha = '02/05/2020'
print (f'Se gastaron {gasto}$.')
print (f'Para la fecha {fecha} el saldo es de {saldo}$.\n')
