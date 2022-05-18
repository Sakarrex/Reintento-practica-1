import csv
from ClaseRepartidor import Repartidor
from ClaseManejadorDePedidos import ManejadorDePedidos


class ManejadorDeRepartidores:
    __ListaRepartidores = []
    __ManejadorP = ManejadorDePedidos()

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

    def InformarRepartidores(self):
        print("Listado Repartidores: ")
        for i in range(len(self.__ListaRepartidores)):
            Total = 0
            print("Apellido: {}                Nombre: {}".format(self.__ListaRepartidores[i].getApellido(), self.__ListaRepartidores[i].getNombre()))
            print("Telefono: {}                Tipo de movilidad".format(self.__ListaRepartidores[i].getTelefono(),self.__ListaRepartidores[i].getTipoMovilidad()))
            print("   Numero de pedido            Descripcion             Cantidad                Precio Unitario                 Total")
            for j in range(self.__ManejadorP.getCantidadDePedidos()):
                PedidoActual = self.__ManejadorP.getPedido(j)
                if PedidoActual.getIdRepartidor() == self.__ListaRepartidores[i].getId() and PedidoActual.getEstado() == "E":
                    print("       {}                   {}               {}                      {}                    {}".format(PedidoActual.getIdPedido(),PedidoActual.getDescripcion(),PedidoActual.getCantidad(), PedidoActual.getPrecioUniatario(),PedidoActual.getCantidad() * PedidoActual.getPrecioUniatario()))
                    Total += PedidoActual.getCantidad() * PedidoActual.getPrecioUniatario()
            print("                                                                                                              Total: " + str(Total))
            print("Importe a pagar por comision: " + str(Total*0.05))
            self.__ListaRepartidores[i].actualizarComision(Total*0.05)
    
    @classmethod
    def ListarPorComision(cls):
        cls.__ListaRepartidores.sort()
        for i in range(len(cls.__ListaRepartidores)):
            print("Id: {}, Nombre: {}, Apellido: {}, Comision: {}".format(cls.__ListaRepartidores[i].getId(),cls.__ListaRepartidores[i].getNombre(),cls.__ListaRepartidores[i].getApellido(),cls.__ListaRepartidores[i].getComision()))