from Animal import Animal

class Hamster(Animal):
    tipo = 'Hamster'
    def __init__(self, nombre, edad, sexo, raza, vacunas, owner, owner_phone, pelaje, dientes):
        super().__init__(nombre, edad, sexo, raza, vacunas, owner, owner_phone)
        self.pelaje = pelaje
        self.dientes = dientes
        
    def mostrar(self):
        return (f'Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nAnimal domesticado: {self.domestico}\nPelaje: {self.pelaje}\nRaza: {self.raza}\nDientes: {self.dientes}')
    
    def comida(self):
        print('El hamster come semillas.')
        