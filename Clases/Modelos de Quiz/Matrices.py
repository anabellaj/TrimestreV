# 

lista_vacia = []
matriz = [[12,14,21],[15,9,36],[18,25,8]]
for lista in matriz:
    for elemento in lista:
        for n in range(2, elemento+1):
            if int(elemento)%int(n) == 0:
                print (n)
