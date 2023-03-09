from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color,capacidad):
        super().__init__(codigo_producto, precio, marca, color)
        self.capacidad = capacidad
        
    def mostrar(self):
        print(f"Codigo del producto: {self.codigo_producto}\nPrecio: {self.precio}\nMarca: {self.marca}\nColor: {self.color}\nCapacidad: {self.capacidad}\n")    
