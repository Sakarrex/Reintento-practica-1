from msilib.schema import SelfReg
from time import sleep


class Repartidor:
    __IdRepartidor = int
    __apellido = str
    __nombre = str
    __telefono = str
    __tipoDeMovilidad = str
    __comision = int
    
    def __init__(self, idRepartidor = -1, apellido = "vacio", nombre ="vacio", telefono="vacio", Movilidad = "vacio", comision = 0):
        self.__IdRepartidor = int(idRepartidor)
        self.__apellido = str(apellido)
        self.__nombre = str(nombre)
        self.__telefono = str(telefono)
        self.__tipoDeMovilidad = str(Movilidad)
        self.__comision = comision

    def __str__(self):
        return "Id: {} Nombre: {} Apellido: {} Telefono: {}".format(self.__IdRepartidor,self.__nombre,self.__apellido,self.__telefono)

    def getId(self):
        return self.__IdRepartidor

    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getTelefono(self):
        return self.__telefono
    
    def getTipoMovilidad(self):
        return self.__tipoDeMovilidad
    
    def getComision(self):
        return self.__comision
    
    def actualizarComision(self,comision):
        self.__comision = comision
    
    def __gt__ (self, otro):
        if type(otro) == Repartidor:
            return self.__comision < otro.getComision()
    
    def __eq__(self, otro):
        if type(otro) == Repartidor:
            return bool(self.__nombre == otro.getNombre() and self.__apellido == otro.getApellido() and self.__telefono == otro.getTelefono())