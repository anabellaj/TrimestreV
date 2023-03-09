from Plantas import Plantas

class Flor(Plantas):
    type = 'flower'
    def __init__(self, id, name, stock, colors):
        super().__init__(id, name, stock)
        self.colors = colors
        
    def mostrar(self):
        print(f"\nID: {self.id}\nType: {self.type}\nName: {self.name}\nStock: {self.stock}")
        print('Colors: ',end='')
        contador = 1
        for color in self.colors:
            if contador < len(self.colors):
                print(color, end=' - ')
            else:
                print(color)
            contador +=1