PEDIDO=("pequeño","mediano","grande")
SECTOR=("centro","norte","sur")
def Registrar_pedidos( clientes,contP,contM,contG) :
    print("Registros de pedidos")
    nombre=input("Ingrese Nombre y Apellido: ").lower(). split()
    direccion=input("Ingrese su Direccion: ").lower()
    sector=input("Ingrese sector: ").lower()
    while sector not in SECTOR:
        print("Sector ingresado NO existe, porfavor intente nuevamente")
        sector=input("Ingrese sector: ").lower()
    
    pedido=input("Ingrese su pedido (Pequeno,Mediano,Grande) : ").lower()
    if pedido == "pequeno" :
        contP=contP+1
    elif pedido == "mediano" :
        contM=contM+1
    else:
        contG=contG+1

    while pedido not in PEDIDO:
        print("Pedido no existente, porfavor vuelva a ingresar")
        pedido=input("Ingrese su pedido (Pequeno,Mediano,Grande) :  ")
        if pedido == "pequeno" :
            contP=contP+1
        elif pedido == "mediano" :
            contM=contM+1
        else:
            contG=contG+1
            
    
    clientes.append({
        "Nombre": nombre,
        "Direccion": direccion,
        "Sector" : sector,
        "Pedido" : pedido

    })

def listar_pedidos(clientes):
    for CLIENTE in clientes :
        print(CLIENTE)



def imprimir_hoja(clientes,contP,contM,contG):
    sector_seleccionado=input("Ingrese el sector que desea imprimir, si desea imprimir todos presione ENTER :")
    if sector_seleccionado == "":
        sector_a_imprimir=clientes
        nombreArchivo='planilla de todos.txt'
    elif sector_seleccionado == SECTOR :
        sector_a_imprimir=[]
        for CLIENTES in sector_a_imprimir :
            if CLIENTES["Sector"] == sector_seleccionado:
                sector_a_imprimir.append(CLIENTES)
                nombreArchivo = (f'planilla de {sector_seleccionado}.txt')


    with open(nombreArchivo,"w") as archivo:
        for CLIENTES in clientes:

            archivo.write (f'Nombre y Apellido: {CLIENTES["Nombre"]}\n')
            archivo.write (f'Direccion: {CLIENTES["Direccion"]}\n')
            archivo.write (f'Sector :{CLIENTES["Sector"]}\n')
            archivo.write (f'Pedido:{CLIENTES["Pedido"]}\n \n')
            archivo.write(f'Paquetes: Pequeño -' [contP] ,'Mediano -' [contM], "Grande -",[contG])
         
