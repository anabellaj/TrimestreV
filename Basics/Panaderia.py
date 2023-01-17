# Cada canilla vale 3.49$. Si el pan no es del dia tiene un descuento del 60%. 
# Introducir el numero de canillas vendidas que no son del dia, imprimir el precio normal y el precio
# con el descuento aplicado. 

canillas = input('Ingrese la cantidad de canillas viejas vendidas:\n>')
while not canillas.isnumeric():
    canillas = input('Ingrese la cantidad de canillas viejas vendidas:\n>')

canillas = int(canillas)
precio = 3.49
descuento = round(3.49*0.6, 2)
costo = precio -descuento
print(f'Se vendieron {canillas} canillas. Originalmente cada una cuesta {precio}$, pero al no ser frescas cuestan {descuento}$.')
ventas = round(costo * canillas, 2)
print(f'El total de ventas fue de {ventas}$.')