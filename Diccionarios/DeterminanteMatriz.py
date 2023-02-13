matriz = [[1, 3, 2], [4, 5, 7], [8, 6, 9]]



def determinante():
    """
    Función que calcula el determinante de una matriz de 3x3 utilizando el método de Sarrus.

    Argumentos => n/a

    Retorna => determinante de la matriz calculado a partir de la suma de los productos de los elementos de sus diagonales.

    """

    # se define una variable para llevar la suma de los productos
    determinante = 0
    
    # se crea una lista vacía auxiliar para aplicar el método de Sarrus posteriormente (agregar al final de la matriz las dos primeras filas o columnas (filas en este caso) y de esa forma calcular los productos con diagonales completas)
    aux = []

    # se añaden a la lista las tres filas originales de la matriz y las dos primeras, de nuevo, al final
    aux.append(matriz[0])
    aux.append(matriz[1])
    aux.append(matriz[2])
    aux.append(matriz[0])
    aux.append(matriz[1])

    # primero se calcularán los tres productos que se suman (diagonal principal y paralelas). Se recore la matriz original (porque se calculan las tres diagonales). Para cada primer elemento de la fila en la que se está trabajando, éste se multiplica por el segundo elemento de la fila de abajo y por el tercer elemento de la fila debajo de esta. Ese resultado se le suma a la variable determinante
    for i,fila in enumerate(matriz):
        prod = fila[0]*aux[i+1][1]*aux[i+2][2]
        determinante += prod


    # luego se calculan los tres productos que se restan (diagonal del lado opuesto). Se recore la matriz original (porque se calculan las tres diagonales). Para cada tercer elemento de la fila en la que se está trabajando, éste se multiplica por el segundo elemento de la fila de abajo y por el primer elemento de la fila debajo de esta. Este resultado se le resta a la variable determinante
    for i, fila in enumerate(matriz):
        prod = fila[2]*aux[i+1][1]*aux[i+2][0]
        determinante -= prod


    # se retorna el resultado
    return determinante



def main():
    # se imprime el resultado
    print(f"Determinante: {determinante()}")

main()