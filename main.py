from ClaseManejadorDePedidos import ManejadorDePedidos
from ClaseManejadorDeRepartidores import ManejadorDeRepartidores

if __name__ == "__main__":
    ManejadorP = ManejadorDePedidos()
    ManejadorR = ManejadorDeRepartidores()
    ManejadorP.Carga()
    ManejadorR.Cargar()
    switch = int(input("1: Obtener Pedidos pendientes de un repartidor\n2: Listar repartidores\n3: Eliminar repartidor repetido\n4: Listar repartidores por comision\n"))
    while switch != 0:
        if switch == 1:
            ManejadorP.InformarPedidosPendientes(int(input("Ingresar numero de repartidor: ")))
        elif switch == 2:
            ManejadorR.InformarRepartidores()
        elif switch == 3:
            print("c")
        elif switch == 4:
            ManejadorR.ListarPorComision()
        else:
            print("Codigo Erroneo")
        switch = int(input("1: Obtener Pedidos pendientes de un repartidor\n2: Listar repartidores\n3: Eliminar repartidor repetido\n4: Listar repartidores por comision\n"))
        