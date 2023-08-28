class Marca:
    def __init__(self, nombre):
        self.__nombre=nombre
    
    def setNombre(self, marca):
        self.__nombre=marca
    
    def getNombre(self):
        return self.__nombre