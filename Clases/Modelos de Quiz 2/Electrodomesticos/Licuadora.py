from Electrodomestico import Electrodomestico

class Licuadora(Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color,material_vaso, velocidades):
        super().__init__(codigo_producto, precio, marca, color)
        self.material_vaso = material_vaso
        self.velocidades = velocidades
        
    def mostrar(self):
        print(f"Codigo del producto: {self.codigo_producto}\nPrecio: {self.precio}\nMarca: {self.marca}\nColor: {self.color}\nMaterial del vaso: {self.material_vaso}\nVelocidades: {self.velocidades}\n")
        
            
