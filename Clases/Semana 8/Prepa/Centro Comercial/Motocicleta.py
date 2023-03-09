from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
   def __init__(self, tipo, placa, marca, puesto, hora_entrada, hora_salida):
      super().__init__(tipo, placa, marca, puesto, hora_entrada, hora_salida)
   
   # def mostrar(self):
   #    print(f"Placa: {self.placa}\nMarca: {self.marca}\nPuesto: {self.puesto}\nHora de entrada: {self.hora_entrada}")
   #    if self.hora_entrada != '':
   #       print(f"Hora de salida: {self.hora_salida}\n")