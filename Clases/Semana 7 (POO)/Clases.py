# Una clase es una estructura en donde se definen los metodos (acciones) y atributos del objeto
# Siempre se debe utilizar siempre el metodo self para establecer los atributos
# Para hacer los atributos privados ponemos __ despues del self. 

# Por ejemplo
class Vehicle:
    def __init__(self, brand, model, color, year):
        self.__brand = brand
        self.model = model
        self.color = color
        self.year = year 

    def get_brand (self):
        return self.__brand 