from Electrodomestico import Electrodomestico

class Microondas (Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color, control):
        super().__init__(codigo_producto, precio, marca, color)
        self.control = control
        
    def mostrar(self):
        print(f"Codigo del producto: {self.codigo_producto}\nPrecio: {self.precio}\nMarca: {self.marca}\nColor: {self.color}")
        if self.control:
            print('Posee control\n')    
        else:
            print('No posee control\n')