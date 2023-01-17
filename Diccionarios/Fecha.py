# Ingresar fecha en formato dd/mm/aaaa e imprimir dd de mes de aaaa

meses = {
    '01': 'enero',
    '02': 'febrero',
    '03': 'marzo',
    '04': 'abril',
    '05': 'mayo',
    '06': 'junio',
    '07': 'julio',
    '08': 'agosto',
    '09': 'septiembre',
    '10': 'octubre',
    '11': 'noviembre',
    '12': 'diciembre',
}

fecha = input('Please enter a date in the format dd/mm/yyyy\n>>')
separar = fecha.split('/')
dia = separar [0]
mes = separar[1]
year = separar[2]

print (dia, 'de', meses[mes], 'de', year +'.')