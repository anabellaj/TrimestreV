class Tiendas:
    def __init__(self, nombre, tipo,piso,rif,owner,owner_phone):
        self.nombre = nombre
        self.tipo = tipo
        self.piso = piso
        self.rif = rif
        self.owner = owner
        self.owner_phone = owner_phone
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}\nTipo: {self.tipo}\nPiso: {self.piso}\nRIF: {self.rif}\nNombre del dueño: {self.owner}\nTelefono del dueño: {self.owner_phone}")
        

        
        