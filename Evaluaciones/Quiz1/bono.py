matrix_1 = [ [ "+", "+", "-", "+"], [ "+", "+", "+", "+"], [ "+", "+", "+", "+"], [ "+", "+", "+", "+"] ]
matrix_2 = [ [ "a", "a", "a", "a", "a", "a"], [ "a", "a", "a", "a", "a", "a"], [ "a", "a", "a", "a", "z", "a"] ]
matrix_3 = [ [ "O", "O" ], [ "O", "X" ], [ "O", "O" ], [ "O", "O" ], [ "O", "O" ] ]
stop = False
x,y = 0, 1
for fila in matrix_1:
    x+=1
    y = 1
    for elemento in fila:
        if elemento == '+':
            y+=1
        else: 
            print (x,y)
            stop = True
            break
    if stop == True:
        break

stop = False
x,y = 0, 1
for fila in matrix_2:
    x+=1
    y=1
    for elemento in fila:
        if elemento == 'a':
            y+=1
        else: 
            print (x,y)
            stop = True
            break
    if stop == True:
        break
stop = False
x,y = 0, 1
for fila in matrix_3:
    x+=1
    y=1
    for elemento in fila:
        if elemento == 'O':
            y+=1
        else:
            stop = True 
            print (x,y)
            break
    if stop == True:
        break
