lista = [5,3,3,2,4,1]
for i in range(len(lista)):
    for j in range (len(lista) -1):
        if lista[j] > lista[j+1]:
            t = lista[j]
            lista[j] = lista[j+1]
            lista[j] = t
print (lista)
