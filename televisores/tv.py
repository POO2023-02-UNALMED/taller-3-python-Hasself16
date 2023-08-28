class TV:
    numTV=0
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    @classmethod
    def setNumTV(cls,numero):
        cls.numTV=numero 

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        self.__control = None
        TV.numTV += 1

    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca

    def getCanal(self):
        return self.__canal

    def setPrecio(self, precio):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def getVolumen(self):
        return self.__volumen

    def setControl(self, control):
        self.__control = control

    def getControl(self):
        return self.__control
    
    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def getEstado(self):
        return self.__estado

    def setCanal(self,canal):
        if canal>=1 and canal<=120 and self.__estado:
            self.__canal=canal
    
    def canalUp(self):
        if self.__canal<120 and self.__estado:
            self.__canal += 1

    def canalDown(self):
        if self.__canal>1 and self.__estado:
            self.__canal -= 1

    def setVolumen(self,volumen):
        if volumen>=0 and volumen<=7 and self.__estado:
            self.__volumen=volumen

    def volumenUp(self):
        if self.__volumen < 7 and self.__estado:
            self.__volumen += 1

    def volumenDown(self):
        if self.__volumen > 0 and self.__estado:
            self.__volumen -= 1 
