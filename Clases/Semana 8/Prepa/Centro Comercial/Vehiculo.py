class Vehiculo:
    def __init__(self,tipo, placa, marca, puesto, hora_entrada, hora_salida):
        self.placa = placa
        self.marca = marca
        self.puesto = puesto
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.tipo = tipo
    def mostrar(self):
        print(f"Placa: {self.placa}\nMarca: {self.marca}\nPuesto: {self.puesto}\nHora de entrada: {self.hora_entrada}")
        if self.hora_salida != '':
            print(f"Hora de salida: {self.hora_salida}\n")
            
    
