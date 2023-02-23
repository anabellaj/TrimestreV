def get_lista():
    lista = []
    while True:
        try:
            long = int(input('Ingrese la longitud deseada de su lista\n>> '))
            break
        except:
            print('Por favor solo ingrese números enteros')
    vueltas = 1
    while len(lista) < long:
        while True:
            try:
                num = int(input(f'Ingrese el número {vueltas} de su lista\n>> '))
                break
            except:
                print ('Por favor ingrese solo números enteros')
        lista.append(num)
        vueltas += 1
    return lista

def sort_list(lista):
    lista.sort()
    for n in lista:
        if lista.count(n) > 1:
            lista.remove(n)
    return lista

def main():
    lista = get_lista()
    lista_ordenada = sort_list(lista)
    print(lista_ordenada)
main()