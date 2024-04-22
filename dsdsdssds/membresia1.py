from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self._correo_suscriptor = correo_suscriptor
        self._numero_tarjeta = numero_tarjeta
    #getter
    @property
    def correo_suscriptor(self):
        return self._correo_suscriptor
    
    @property
    def numero_tarjeta(self):
        return self._numero_tarjeta
    #metodo abstracto
    @abstractmethod
    def cambiar_suscripcion(self, tipo: int):
        pass
    
    def cancelar_suscripcion(self):
        # Método para cancelar la suscripción y crear una nueva membresía de tipo Gratis
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
    
"""a. Heredar la o las clases necesarias para evitar repetir implementaciones.
b. Definir los atributos de clase necesarios.
c. Definir los métodos necesarios (en caso de que se justifique).
d. Sobrescribir los métodos necesarios (en caso de que se justifique).
"""
class Gratis(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 0
        self._max_dispositivos = 1
    
    def cambiar_suscripcion(self, tipo: int):
        if tipo in range(1, 5):
            return self._crear_nueva_membresia(tipo)
        else:
            return self

    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

class Basica(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 3000
        self._max_dispositivos = 2
    
    def cambiar_suscripcion(self, tipo: int):
        if tipo in range(2, 5):
            return self._crear_nueva_membresia(tipo)
        else:
            return self

    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

class Familiar(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 5000
        self._max_dispositivos = 5
        self._dias_regalo = 7
    
    def cambiar_suscripcion(self, tipo: int):
        if tipo in [1, 3, 4]:
            return self._crear_nueva_membresia(tipo)
        else:
            return self

    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

    def modificar_control_parental(self):
        pass

class SinConexion(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 3500
        self._max_dispositivos = 2
        self._dias_regalo = 7
    
    def cambiar_suscripcion(self, tipo: int):
        if tipo in [1, 2, 4]:
            return self._crear_nueva_membresia(tipo)
        else:
            return self

    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

    def aumentar_contenido_sin_conexion(self):
        pass

class Pro(Familiar, SinConexion):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._costo = 7000
        self._max_dispositivos = 6
        self._dias_regalo = 15
    
    def cambiar_suscripcion(self, tipo: int):
        if tipo in range(1, 4):
            return self._crear_nueva_membresia(tipo)
        else:
            return self

    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif tipo == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)

    def modificar_control_parental(self):
        pass

    def aumentar_contenido_sin_conexion(self):
        pass
    
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