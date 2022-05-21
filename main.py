from ClaseManejadorDePedidos import ManejadorDePedidos
from ClaseManejadorDeRepartidores import ManejadorDeRepartidores

if __name__ == "__main__":
    ManejadorPedidos = ManejadorDePedidos()
    ManejadorR = ManejadorDeRepartidores()
    ManejadorPedidos.Carga()
    ManejadorR.Cargar()
    switch = int(input("1: Obtener Pedidos pendientes de un repartidor\n2: Listar repartidores\n3: Eliminar repartidor repetido\n4: Listar repartidores por comision\n"))
    while switch != 0:
        if switch == 1:
            ManejadorPedidos.InformarPedidosPendientes(int(input("Ingresar numero de repartidor: ")))
        elif switch == 2:
            ManejadorR.InformarRepartidores(ManejadorPedidos)
        elif switch == 3:
            ManejadorR.EliminarRepartidor(int(input("Ingresar codigo de repartidor a eliminar: ")),ManejadorPedidos)
        elif switch == 4:
            ManejadorR.ListarPorComision()
        elif switch == 5:
            ManejadorR.MostrarRepartidores()
        else:
            print("Codigo Erroneo")
        switch = int(input("1: Obtener Pedidos pendientes de un repartidor\n2: Listar repartidores\n3: Eliminar repartidor repetido\n4: Listar repartidores por comision\n"))
        