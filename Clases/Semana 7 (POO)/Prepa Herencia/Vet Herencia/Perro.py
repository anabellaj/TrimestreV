from Animal import Animal

class Perro(Animal):
    tipo = 'Perro'
    def __init__(self, nombre, edad, sexo, raza, vacunas, owner, owner_phone, pelaje):
        super().__init__(nombre, edad, sexo, raza, vacunas, owner, owner_phone)
        self.pelaje = pelaje

    def mostrar(self):
        return (f'Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nAnimal domesticado: {self.domestico}\nPelaje: {self.pelaje}\nRaza: {self.raza}\nVacunas: {self.vacunas}\nPropietario: {self.owner}\nNumero del propietario: {self.owner_phone}\n')
    
    
    def comida(self):
        print('El perro come perrarina')