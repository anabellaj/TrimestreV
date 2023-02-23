# en una clase:
#       Atributos de instancia: distintos entre todos los objetos
#       Atributos de clase: el mismo para todos los ohjetos de una clase

class Perro: 
    # Atributo de clase
    especie = 'Mamifero'
    def __init__(self, nombre,raza):
        print(f'Creando perro {nombre}, {raza}')
        
        # Atributos de instancia
        self.nombre = nombre
        self.raza =  raza
        
        # Los metodos funcionan como funciones 
    def ladrar (self):
        print('Guau')
    def caminar (self, pasos):
        print(f'Caminando {pasos} pasos.')
        
mi_perro = Perro('Toby', 'Golden Retriever')
mi_perro.ladrar()
mi_perro.caminar(55)



# Podemos acceder a variables especificas utilizando variable.atributo EJ:
print(mi_perro.nombre)   # Toby  

