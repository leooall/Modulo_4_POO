from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

#Solicita al usuario información sobre la tienda a crear 
def crear_tienda():
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ").lower()
    
    if tipo_tienda == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo_tienda == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo_tienda == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido. Inténtelo de nuevo.")
        return crear_tienda()

# ingresar información sobre un nuevo producto 
def ingresar_producto(tienda):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto (opcional, dejar en blanco para 0): ") or 0)
    
    producto = Producto(nombre, precio, stock)
    tienda.ingresar_producto(producto)

#Muestra una lista de productos disponibles en la tienda especificada
def listar_productos(tienda):
    print("Listado de productos:")
    print(tienda.listar_productos())

def realizar_venta(tienda):# permite  realizar una venta en la tienda especificada
    nombre_producto = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    tienda.realizar_venta(nombre_producto, cantidad)

#Crea una tienda, y luego ejecuta un bucle donde se presentan las opciones al usuario 
# y se llama a las funciones correspondientes según la opción seleccionada.
def main():
    tienda = crear_tienda()
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            ingresar_producto(tienda)
        elif opcion == "2":
            listar_productos(tienda)
        elif opcion == "3":
            realizar_venta(tienda)
        elif opcion == "4":
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
