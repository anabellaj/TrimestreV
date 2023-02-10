# x[::-1] voltea el string, sirve para palindromos
numeros = [111, 15, 952, 7952, 74147, 994442, 0, 963214, 42, 1230, 778877, 95159, 23, 20, 1, 10, 122]
numeros_clasif = {
    "Palíndromos": [ ],
    "Con cifras repetidas": [ ]
}
count = 0
for number in numeros:
    # Palindromo: Igual al derecho y al reves
    test = list(str(number))
    test.reverse()
    compare = str(test)
    if compare == str(list(str(number))):
        for k, v in numeros_clasif.items():
            if k == 'Palíndromos':
                v.append(number)
    # Cifras repetidas
    for cifra in str(number):
        count = str(number).count(str(cifra))
    if count > 1:
        for k, v in numeros_clasif.items():
            if k == 'Con cifras repetidas':
                v.append(number)
print (numeros_clasif)     