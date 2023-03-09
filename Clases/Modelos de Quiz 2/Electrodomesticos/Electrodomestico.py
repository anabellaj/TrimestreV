class Electrodomestico:
    def __init__(self, codigo_producto,precio,marca,color):
        self.codigo_producto = codigo_producto
        self.precio = precio
        self.marca =  marca
        self.color = color
        
    def mostrar(self):
        print(f"Codigo del producto: {self.codigo_producto}\nPrecio: {self.precio}\nMarca: {self.marca}\nColor: {self.color}\n")    
    
    