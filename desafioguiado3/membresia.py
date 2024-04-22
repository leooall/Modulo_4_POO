from abc import ABC, abstractmethod

class Membresia(ABC):
    #constructor
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta
    
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor
    
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    #metodo abstracto
    @abstractmethod
    def cambiar_suscripcion(self, tipo: int):
        pass
    
    def cancelar_suscripcion(self):
        # Método para cancelar la suscripción y crear una nueva membresía de tipo Gratis
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class Gratis(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        # Costo y máximo de dispositivos de una membresía Gratis
        self.costo = 0
        self.max_dispositivos = 1
    
    def cambiar_suscripcion(self, tipo: int):
        # Método para cambiar la suscripción, solo permite cambiar a cualquier tipo de membresía
        # Retorna la membresía actual si el tipo solicitado no es válido
        if tipo in range(1, 5):
            return self._crear_nueva_membresia(tipo)
        else:
            return self

class Basica(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        # Costo y máximo de dispositivos de una membresía Básica
        self.costo = 3000
        self.max_dispositivos = 2
    
    def cambiar_suscripcion(self, tipo: int):
        # Método para cambiar la suscripción
        if tipo in range(2, 5):
            return self._crear_nueva_membresia(tipo)
        else:
            return self

class Familiar(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        # Costo y máximo de dispositivos de una membresía Familiar, también los días de regalo
        self.costo = 5000
        self.max_dispositivos = 5
        self.dias_regalo = 7
    
    def cambiar_suscripcion(self, tipo: int):
        # Método para cambiar la suscripción
        if tipo in [1, 3, 4]:
            return self._crear_nueva_membresia(tipo)
        else:
            return self

    def modificar_control_parental(self):
        # Método para modificar el control parental (aún no implementado)
        pass

class SinConexion(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        # Costo y máximo de dispositivos de una membresía SinConexión, también los días de regalo
        self.costo = 3500
        self.max_dispositivos = 2
        self.dias_regalo = 7
    
    def cambiar_suscripcion(self, tipo: int):
        # Método para cambiar la suscripción
        return self._crear_nueva_membresia(tipo)


    def aumentar_contenido_sin_conexion(self):
        pass

class Pro(Familiar, SinConexion):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        # Costo y máximo de dispositivos de una membresía pro, también los días de regalo
        self.costo = 7000
        self.max_dispositivos = 6
        self.dias_regalo = 15

g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
