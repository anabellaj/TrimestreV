def peticion(mensaje):
    pedir = mensaje
    if mensaje[0] == '.':
        last = len(mensaje) -1
        if mensaje[last] == '.':
            pedir = mensaje.replace(mensaje, 'Pedro por favor responde')
    return pedir        
    
def main():
    pregunta = input('Por favor ingrese su pregunta para Pedro: \n>> ')
    mensaje = input('Por favor ingrese su peticion:\n>> ')
    pedir = peticion(mensaje)
    print('Pregunta:',pregunta,'\n' 'Peticion:', pedir)
    input('Presione cualquier tecla para obtener su respuesta')
    print (mensaje)
    
main()  