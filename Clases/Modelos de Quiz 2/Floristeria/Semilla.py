from Plantas import Plantas

class Semilla(Plantas):
    type = 'seeds'
    def __init__(self, id, name, stock):
        super().__init__(id, name, stock)
        
    def mostrar(self):
        print(f"\nID: {self.id}\nType: {self.type}\nName: {self.name}\nStock: {self.stock}\n")