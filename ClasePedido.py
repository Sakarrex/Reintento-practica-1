import re


class Pedido:
    __IdRepartidor = int
    __IdPedido = int
    __Descripcion = str
    __cantidad = int
    __precioUnitario = int
    __estado = str

    def __init__(self, idRepartidor = -1, idpedido = -1, descripcion = "vacio", cantidad= -1, precioUnitario = -1, estado = "vacio"):
        self.__IdRepartidor = int(idRepartidor)
        self.__IdPedido = int(idpedido)
        self.__Descripcion = str(descripcion)
        self.__cantidad = int(cantidad)
        self.__precioUnitario = int(precioUnitario)
        self.__estado = str(estado)
    
    def getIdRepartidor(self):
        return self.__IdRepartidor
    
    def getIdPedido(self):
        return self.__IdPedido
    
    def getDescripcion(self):
        return self.__Descripcion
    
    def getCantidad(self):
        return self.__cantidad
    
    def getPrecioUniatario(self):
        return self.__precioUnitario
    
    def getEstado(self):
        return self.__estado
        