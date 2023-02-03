# A partir de la lista proporcionada, tomar cada numero y buscar dos numeros que multiplicados den 
# el numero inicial de la lista. Guardar el par de numeros en una lista dentro de una lista grande
# con todos los pares de numeros. 
numbers = [12,14,21]
for n in numbers:
    for x in range(1, n+1):
        