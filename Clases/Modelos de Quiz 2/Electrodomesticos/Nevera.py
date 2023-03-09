from Electrodomestico import Electrodomestico

class Nevera (Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color, freezer, compartimentos):
        super().__init__(codigo_producto, precio, marca, color)
        self.compartimentos = compartimentos
        self.freezer = freezer
        
    def mostrar(self):
        print(f"Codigo del producto: {self.codigo_producto}\nPrecio: {self.precio}\nMarca: {self.marca}\nColor: {self.color}\nNumero de compartimentos: {self.compartimentos}")
        if self.freezer:
            print('Incluye sistema de freezer\n')
        else:
            print('No incluye sistema de freezer\n')

    