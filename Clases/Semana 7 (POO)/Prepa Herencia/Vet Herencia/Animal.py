# Clase Padre: Animales
            #Atr: nombre,edad,sexo
# Clases hijas: 
#           perros: pelaje,raza
#           loro: plumaje, alas
#           gatos: pelaje, bigotes
#           hamsters: pelaje, dientes

class Animal:
    domestico = True
    def __init__(self, nombre, edad, sexo, raza, vacunas, owner, owner_phone):
        self.nombre = nombre
        self.edad= edad
        self.sexo = sexo
        self.raza = raza
        self.vacunas = vacunas
        self.owner = owner
        self.owner_phone = owner_phone
        
    def mostrar(self):
        return (f'\nNombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nAnimal domesticado: {self.domestico}\nRaza: {self.raza}\nPropietario: {self.owner}\nNumero del propietario: {self.owner_phone}\nVacunas: {self.vacunas}')

    