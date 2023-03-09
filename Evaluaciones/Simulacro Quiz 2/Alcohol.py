from Bebida import Bebida

class Alcohol(Bebida):
    def __init__(self, nombre, marca, disponible, grado, tipo):
        super().__init__(nombre, marca, disponible)
        self.grado = grado
        self.tipo = tipo
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}\nMarca: {self.marca}\nGrado de alcohol: {self.grado}°\nTipo: {self.tipo}")
        if self.disponible:
            print('Esta bebida se encuentra disponible.\n')
        else:
            print('Esta bebida no se encuentra disponible.\n')
        