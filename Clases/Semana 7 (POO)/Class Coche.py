class Coche:
    ruedas = 4
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
        
    def __acelera(self):
        self.velocidad= self.velocidad + self.aceleracion
        
    def frena(self):
        v= self.velocidad - self.aceleracion
        if v<0:
            v=0
        self.velocidad = v
        
c1 = Coche('rojo', 20)
print(c1.color, c1.ruedas, c1.velocidad, c1.aceleracion)
