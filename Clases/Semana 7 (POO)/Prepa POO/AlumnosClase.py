class Alumnos:
    def __init__(self, nombre, grado, promedio, direccion, representante, telefono_rep, beca):
        self.nombre = nombre
        self. grado = grado
        self.promedio = promedio
        self.direccion = direccion
        self.representante = representante
        self.telefono_rep = telefono_rep
        self.beca = beca
        
    def mostrar(self):
        # Metodo que muestra la informacion del objeto de manera ordenada
        print(f"Nombre: {self.nombre}\nGrado: {self.grado}\nPromedio: {self.promedio}\nDireccion: {self.direccion}\nNombre del representante: {self.representante}\nTelefono del representante: {self.telefono_rep}\nCondicion de beca: {self.beca}")
        