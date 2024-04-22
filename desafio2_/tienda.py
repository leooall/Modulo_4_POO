from abc import ABC, abstractmethod
# Definición de la clase abstracta Tienda
class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @abstractmethod
    def ingresar_producto(self, producto):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass
# Definición de la clase Restaurante 
class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        pass

    def listar_productos(self):
        pass

    def realizar_venta(self, nombre_producto, cantidad):
        pass
# Definición de la clase supermercado
class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        pass

    def listar_productos(self):
        pass

    def realizar_venta(self, nombre_producto, cantidad):
        pass
# Definición de la clase farmacia
class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        pass

    def listar_productos(self):
        pass

    def realizar_venta(self, nombre_producto, cantidad):
        pass
