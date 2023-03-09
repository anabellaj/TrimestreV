from Animal import Animal

class Loro(Animal):
    tipo = 'Loro'
    def __init__(self, nombre, edad, sexo, raza, vacunas, owner, owner_phone,plumaje,alas):
        super().__init__(nombre, edad, sexo, raza, vacunas, owner, owner_phone)
        self.plumaje = plumaje
        self.alas = alas
        
    def mostrar(self):
        return (f'Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nAnimal domesticado: {self.domestico}\nPlumaje: {self.plumaje}\nRaza: {self.raza}\nVacunas: {self.vacunas}\nPropietario: {self.owner}\nNumero del propietario: {self.owner_phone}\nAlas: {self.alas}')
    
    
    def comida(self):
        print('El loro come cambur.')