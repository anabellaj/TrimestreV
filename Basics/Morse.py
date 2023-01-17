# Decifrar codigo morse
morse = {
    '_____': '0',
    '.____': '1',
    '..___': '2',
    '...__': '3',
    '...._': '4',
    '.....': '5',
    '_....': '6',
    '__...': '7',
    '___..': '8',
    '____.': '9'
}

lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
codigo1 = ''
codigo2 = ''
codigo3 = ''
codigo4 = ''
codigo5 = ''
codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____.*"
post = codigos_postales.split('*')
for numbers in post:
    num = numbers.split()
    for n in num:
        if n in morse:
            final = morse.get(n)
            if len(lista1) < 4:
                lista1.append(final)
            elif len(lista2) < 4:
                lista2.append(final)
            elif len(lista3) < 4:
                lista3.append(final)
            elif len(lista4) < 4:
                lista4.append(final)
            elif len(lista5) < 4:
                lista5.append(final) 

print ('Los codigos postales son:')
for num in lista1:
    codigo1 += num 
for num in lista2:
    codigo2 += num 
for num in lista3:
    codigo3 += num 
for num in lista4:
    codigo4 += num 
for num in lista5:
    codigo5 += num 
print (f'{codigo1}, {codigo2}, {codigo3}, {codigo4}, {codigo5}')
