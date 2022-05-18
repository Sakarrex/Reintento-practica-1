import csv

import numpy
from ClasePedido import Pedido

class ManejadorDePedidos:
    __cantidadDePedidos = 16
    __ArregloPedidos = numpy.empty(16, dtype= Pedido)

    def Carga(self):
        __archivo = open("pedidos.csv")
        __reader = csv.reader(__archivo, delimiter = ";")

        i=0
        bandera = False
        for files in __reader:
            if bandera == False:
                bandera = True
            else:
                UnPedido = Pedido(files[0],files[1],files[2],files[3],files[4],files[5])
                self.__ArregloPedidos[i] = UnPedido
                i+=1
        __archivo.close
    
    @classmethod
    def InformarPedidosPendientes(cls, idRepartidor):
        print("Pedidos pendientes: ")
        for i in range(cls.__cantidadDePedidos):
            if cls.__ArregloPedidos[i].getIdRepartidor() == idRepartidor and cls.__ArregloPedidos[i].getEstado() == "N":
                print("Id de pedido: " + str(cls.__ArregloPedidos[i].getIdPedido()) + " Descripcion: " + cls.__ArregloPedidos[i].getDescripcion())

    @classmethod
    def getCantidadDePedidos(cls):
        return cls.__cantidadDePedidos
    

    def getPedido(self, numeropedido):
        return self.__ArregloPedidos[numeropedido]