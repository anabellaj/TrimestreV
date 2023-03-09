from Bebida import Bebida

class Refresco(Bebida):
    def __init__(self, nombre, marca, disponible, azucar, sabor):
        super().__init__(nombre, marca, disponible)
        self.azucar = azucar
        self.sabor = sabor
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}\nMarca: {self.marca}\nPorcentaje de azucar: {self.azucar}%\nSabor: {self.sabor}")
        if self.disponible:
            print('Esta bebida se encuentra disponible.\n')
        else:
            print('Esta bebida no se encuentra disponible.\n')    