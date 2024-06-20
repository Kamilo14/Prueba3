import Funciones1 as fn 

clientes =[]
contP=0
contM=0
contG=0

while True:
    try:
        print("                     MENU            ")
        print("*************************************")
        print("1. Registrar pedido")
        print("2. Lista todo los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir de Programa")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1 :
            fn.Registrar_pedidos( clientes,contP,contM,contG)
        elif opcion == 2:
            fn.listar_pedidos(clientes)
        elif opcion == 3 :
            fn.imprimir_hoja(clientes,contP,contM,contG)
        elif opcion == 4 :
            print("Saliendo.....")
    except ValueError:
        print("Debe ingresar una opcion entre el 1 y 4 ")