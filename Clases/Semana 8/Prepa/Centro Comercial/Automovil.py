from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, tipo, placa, marca, puesto, hora_entrada, hora_salida,minusvalido):
        super().__init__(tipo, placa, marca, puesto, hora_entrada, hora_salida)
        self.minusvalido = minusvalido
        
    def mostrar(self):
        print(f"Placa: {self.placa}\nMarca: {self.marca}\nPuesto: {self.puesto}\nMinusvalido: {self.minusvalido}\nHora de entrada: {self.hora_entrada}")
        if self.hora_salida != '':
            print(f"Hora de salida: {self.hora_salida}\n")