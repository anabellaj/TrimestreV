class Plantas:
    def __init__(self, id, name, stock):
        self.id = id
        self.name = name
        self.stock = stock
        
    def mostrar(self):
        print(f"ID: {self.id}\nName: {self.name}\nStock: {self.stock}\n")