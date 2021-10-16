from collections import namedtuple
import datetime

Ticket = namedtuple("Ticket", ("fecha", "descripcion", "cantidad", "precio"))

ventas = {}

continuar = True

while continuar:
    respuesta = 1
    menu = int(input('''
===============================================
                    MENU
===============================================
 
1.- Registrar venta
2.- Consultar ventas
3.- Salir

Seleccione la opcion que desea: '''))
    
    if menu == 1:
        while True:
            while respuesta == 1:
                respuesta2 = 1
                tupla_folio = ()
                tupla_tuplaNominada = ()
                while respuesta2 == 1:
                    folio = int(input("\nIngrese el folio de venta: "))      
                    tupla_folio = tupla_folio + (folio,)
                    fecha_venta = datetime.date.today()
                    descripcion_venta = str(input("Ingrese el articulo: "))
                    cantidad_venta = int(input("Ingrese la cantidad de articulos: "))
                    precio1 = int(input("Ingrese el precio individual: "))
                    precio2 = precio1 * cantidad_venta
                    IVA = precio2 * 0.16
                    precio_venta = precio2 + IVA
                    venta = Ticket(fecha_venta, descripcion_venta, cantidad_venta, precio_venta)
                    tupla_tuplaNominada = tupla_tuplaNominada + (venta,)
                    print(f"El subtotal es de: {precio2}")
                    print(f"El IVA aplicable es de: {IVA}")
                    print(f"El precio total es de: {precio_venta}")
                    respuesta2 = int(input("¿Quiere seguir registrando articulos? [0 = NO, 1 = SI]: "))
                    if respuesta2 == 0 :
                        ventas[tupla_folio] = tupla_tuplaNominada
                        print("Se ha registrado la venta exitosamente")
                respuesta = int(input("¿Quiere seguir registrando ventas? [0 = NO, 1 = SI]: "))
                if respuesta == 0: break
            break
        
    elif menu == 2:
        print("\nListado completo de ventas:")
        for folio in ventas.keys():
            precio_total = 0
            contador = 0
            contador1 = len(ventas[folio])
            print(f"Folio: {folio}")
            print(f"Fecha: {ventas[folio][contador].fecha}")
            while contador < contador1:
                print(f"Descripcion: {ventas[folio][contador].descripcion}")
                print(f"Cantidad: {ventas[folio][contador].cantidad}")
                print(f"Precio: {ventas[folio][contador].precio}")
                precio_total = precio_total + ventas[folio][contador].precio
                contador = contador + 1
            print(f"Precio Total: {precio_total}")
            print()
            
    elif menu == 3:
        print("¡Gracias por usar nuestro sistema!")
        continuar = False
        
    else:
        print("Opcion no valida")
        