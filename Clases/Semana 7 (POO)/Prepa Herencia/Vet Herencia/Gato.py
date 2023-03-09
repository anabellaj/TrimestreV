from Animal import Animal


class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, edad, sexo, raza, vacunas, owner, owner_phone, pelaje, estado_bigote, cut_nails):
        super().__init__(nombre, edad, sexo, raza, vacunas, owner, owner_phone)
        self.pelaje = pelaje
        self.estado_bigote = estado_bigote
        self.cut_nails = cut_nails
        
    def mostrar(self):
        return (f'Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nAnimal domesticado: {self.domestico}\nPelaje: {self.pelaje}\nRaza: {self.raza}\nVacunas: {self.vacunas}\nPropietario: {self.owner}\nNumero del propietario: {self.owner_phone}\nEstado de los bigotes: {self.estado_bigote}\nCorte de uñas: {self.cut_nails}')
    
    def comida(self):
        print('El gato come gatarina.')

        
        