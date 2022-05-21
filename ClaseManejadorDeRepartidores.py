import csv

from ClaseRepartidor import Repartidor



class ManejadorDeRepartidores:
    __ListaRepartidores = []
    

    def __init__(self):
        self.__ListaRepartidores = []

    def Cargar(self):
        __archivo = open("repartidores.csv")
        __reader = csv.reader(__archivo, delimiter=";")

        bandera = False
        for file in __reader:
            if bandera == False:
                bandera = True
            else:
                self.__ListaRepartidores.append(Repartidor(file[0],file[1],file[2],file[3],file[4],file[5]))
        __archivo.close

    def InformarRepartidores(self, ManejadorP):
        print("Listado Repartidores: ")
        for i in range(len(self.__ListaRepartidores)):
            Total = 0
            print("Apellido: {}                Nombre: {}".format(self.__ListaRepartidores[i].getApellido(), self.__ListaRepartidores[i].getNombre()))
            print("Telefono: {}                Tipo de movilidad".format(self.__ListaRepartidores[i].getTelefono(),self.__ListaRepartidores[i].getTipoMovilidad()))
            print("   Numero de pedido            Descripcion             Cantidad                Precio Unitario                 Total")
            for j in range(ManejadorP.getCantidadDePedidos()):
                PedidoActual = ManejadorP.getPedido(j)
                if PedidoActual.getIdRepartidor() == self.__ListaRepartidores[i].getId() and PedidoActual.getEstado() == "E":
                    print("       {}                   {}               {}                      {}                    {}".format(PedidoActual.getIdPedido(),PedidoActual.getDescripcion(),PedidoActual.getCantidad(), PedidoActual.getPrecioUniatario(),PedidoActual.getCantidad() * PedidoActual.getPrecioUniatario()))
                    Total += PedidoActual.getCantidad() * PedidoActual.getPrecioUniatario()
            print("                                                                                                              Total: " + str(Total))
            print("Importe a pagar por comision: " + str(Total*0.05))
            self.__ListaRepartidores[i].actualizarComision(Total*0.05)
    
    
    def ListarPorComision(self):
        self.__ListaRepartidores.sort()
        for i in range(len(self.__ListaRepartidores)):
            print("Id: {}, Nombre: {}, Apellido: {}, Comision: {}".format(self.__ListaRepartidores[i].getId(),self.__ListaRepartidores[i].getNombre(),self.__ListaRepartidores[i].getApellido(),self.__ListaRepartidores[i].getComision())) 
    
    def EliminarRepartidor(self,idRepartidor, ManejadorP):
        auxRepartidor = None
        auxPosicionRepartidor = -1
        bandera1 = False
        i = 0
        while i < len(self.__ListaRepartidores) and bandera1 == False:
            if self.__ListaRepartidores[i].getId() == idRepartidor:
                auxRepartidor = self.__ListaRepartidores[i]
                auxPosicionRepartidor = i
                bandera1 = True
            i+=1
        
        
        if auxRepartidor != None:
            j = 0
            bandera2 = False
            while j < len(self.__ListaRepartidores) and bandera2 == False:
                if auxRepartidor == self.__ListaRepartidores[j]:
                    if ManejadorP.getPedidosPendientes(idRepartidor) == True:
                        self.__ListaRepartidores.pop(auxPosicionRepartidor)
                        print("Repartidor eliminado corretamente")
                    else:
                        print("No es posible eliminar repartidor ya que posee pedidos pendientes")
                    bandera2 == True
                j+=1
        else:
            print("Repartidor no encontrado")
    
    def MostrarRepartidores(self):
        for i in range(len(self.__ListaRepartidores)):
            print(self.__ListaRepartidores[i])