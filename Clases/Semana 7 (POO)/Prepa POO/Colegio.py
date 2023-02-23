# Organizar la base de datos de alumnos de un colegio

from AlumnosClase import Alumnos

def registrar_alumnos(students):
    nombre = input('Ingrese el nombre y apellido del alumno:\n>> ').title()
    print('\n1. 1er grado\n2. 2do grado\n3. 3er grado\n4. 4to grado\n5. 5to grado\n6. 6to grado\n7. 1er año\n8. 2do año\n9. 3er año\n10. 4to año\n11. 5to año')
    while True:
        try:  
            grado = int(input('Introduzca el numero correspondiente al grado del alumno:\n>> '))
            if grado not in range(1,12):
                raise Exception
            break
        except:
            print('ERROR\nPor favor ingrese una opcion valida')
    if grado == 1:
        grado = '1ero'      
    elif grado == 2:
        grado = '2do'
    elif grado == 3:
        grado = '3ero'
    elif grado == 4:
        grado = '4to'
    elif grado == 5:
        grado = '5to'
    elif grado == 6:
        grado = '6to'
    elif grado == 7:
        grado = '7mo'
    elif grado == 8:
        grado = '8vo'
    elif grado == 9:
        grado = '9no'
    elif grado == 10:
        grado = '4to año'
    elif grado == 11:
        grado = '5to año'  
    while True:
        try:
            promedio = float(input('Por favor ingrese el promedio del alumno:\n>> '))
            if promedio > 20 or promedio < 0:
                raise Exception
            break
        except:
            print('ERROR - Recuerde que el promedio debe encontrarse entre los valores del 0 y del 20')
    direccion = input('Por favor ingrese la direccion del alumno:\n>> ').title()
    representante = input('Por favor ingrese el nombre y apellido del representante del alumno:\n>> ').title()
    while True:
        try:
            telefono_rep = int(input('Por favor ingrese el numero del representante del alumno:\n>> '))
            if len(str(telefono_rep)) not in range(10,12):
                raise Exception
            break
        except:
            print('ERROR - Por favor ingrese un numero de telefono valido')
    beca = False
    if promedio > 18:
        beca = True
    nuevo_alumno = Alumnos(nombre, grado, promedio,direccion,representante,telefono_rep,beca)
    students.append(nuevo_alumno)
    print('\nAlumno registrado con exito!\n')
    nuevo_alumno.mostrar()
    return students

def ver_alumnos(students):
    for i,a in enumerate(students):
        print('------------','Alumno',i+1,'-----------')
        a.mostrar()

def top_cinco (alumnos):
    alumnos.sort(key = lambda alumno: alumno.promedio, reverse=True)
    for i,alumno in enumerate(alumnos):
        if i < 5:
            print('------------','Alumno',i+1,'-----------')
            alumno.mostrar() 
            
def promedio_general(alumnos):
    promedios = []
    for alumno in alumnos:
        promedios.append(alumno.promedio)
    return sum(promedios) / len(promedios)

def clasif_promedio(alumnos):
    men_10, men_16, hasta_20 = 0,0,0
    for a in alumnos:
        if a.promedio < 10:
            men_10+=1
        elif a.promedio < 16:
            men_16+= 1
        else:
            hasta_20+= 1
            
    print('-------ESTADISTICAS-------\nCantidad de alumnos con promedio menor a 10:', men_10,'\nCantidad de alumnos con promedio entre 10 y 16:',men_16,'\nCantidad de alumnos con promedio entre 16 y 20:',hasta_20)

def main():
    print('\nBienvenido! Que desea realizar hoy?')
    alumnos = []
    while True:
        print('\n1. Registrar estudiantes\n2. Ver estudiantes registrados\n3. Ver mejores 5 alumnos\n4. Ver promedio general\n5. Ver cantidad de alumnos por promedio\n6. Salir')
        seleccion = input('Ingrese el numero correspondiente a su seleccion\n>> ')
        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,7)):
            seleccion = input('ERROR - Opcion invalida\nPor favor ingrese el numero correspondiente a su seleccion\n>> ')
        seleccion = int(seleccion)
        #Registrar estudiantes
        if seleccion == 1:
            print('Bienvenido a la base de datos de los estudiantes!')
            registrar_alumnos(alumnos)
            
        # Ver estudiantes registrados
        elif seleccion ==2:
            ver_alumnos(alumnos)
            if len(alumnos) == 0:
                print('Todavia no hay alumnos registrados en la base de datos')
        
        # Ver mejores 5 alumnos
        elif seleccion == 3:
            top_cinco(alumnos)
            if len(alumnos) == 0:
                print('Todavia no hay alumnos registrados en la base de datos')
        
        
        # Promedio general
        elif seleccion == 4:
            if len(alumnos) == 0:
                print('Todavia no hay alumnos registrados en la base de datos')
            print('El promedio general de los alumnos es de', promedio_general(alumnos), 'puntos.')
        
        # Ver cantidad de alumnos por promedio
        elif seleccion == 5:
            clasif_promedio(alumnos)
        
        elif seleccion == 6:
            print('\n\nHasta pronto!\n\n')
            break
        
        
main()