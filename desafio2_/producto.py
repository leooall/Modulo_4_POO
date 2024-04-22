#clase que permite instanciar los productos con su nombre precio y stock
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock

    #metodo para modificar stock
    def modificar_stock(self, cantidad):
        if cantidad < 0:
            cantidad = 0
        self.__stock += cantidad
