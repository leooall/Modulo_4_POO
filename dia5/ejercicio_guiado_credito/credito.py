from abc import ABC, abstractmethod

class SolicitudCredito(ABC):
    
    @abstractmethod
    def validar_monto(self, monto: int):
        pass
    
    @abstractmethod
    def validar_correo(self, correo: str):
        pass
    
    
class SolicitudCreditoDeConsumo(SolicitudCredito):
    __terminaciones = (".cl", ".com")
    def __init__(self, monto: int, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__correo = self.validar_correo(correo)

    def validar_monto(self, monto: int):
        if monto < 1000000:
            monto = 1000000
        elif monto > 5000000:
            monto = 5000000
        return monto
    
    def validar_correo(self, correo: str):
        return correo if (correo.count("@") == 1
                          and correo.endswith(self.__terminaciones)) else ""

    @property
    def monto(self):
        return self.__monto
    
    @property
    def correo(self):
        return self.__correo


class SolicitudCreditoComercial(SolicitudCredito):
    __prohibidos = ("gmail", "outlook", "hotmail")
    __terminaciones = (".cl", ".com", ".org")
    def __init__(self, monto: int, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__correo = self.validar_correo(correo)

    def validar_monto(self, monto: int):
        if monto < 1000000:
            monto = 1000000
        elif monto > 5000000:
            monto = 5000000
        return monto
    
    def validar_correo(self, correo: str):
        return correo if (correo.count("@") == 1
                            and correo.endswith(self.__terminaciones)
                            and not any(p in correo.lower() for p in self.__prohibidos)) else ""

    @property
    def monto(self):
        return self.__monto
    
    @property
    def correo(self):
        return self.__correo
        
        
class SolicitudCreditoHipotecario(SolicitudCredito):
    __terminaciones = (".cl", ".com")
    def __init__(self, monto, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__correo = self.validar_correo(correo)
    @property
    def monto(self):
        return self.__monto
    @monto.setter
    def monto(self, monto: int):
        self.__monto = self.validar_monto(monto)
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self, correo: str):
        self.__correo = self.validar_correo(correo)
    def validar_monto(self, monto: int):
        if monto < 20000000:
            monto = 20000000
        elif monto > 100000000:
            monto = 100000000
        return monto
    def validar_correo(self, correo: str):
        return (correo if correo.count("@") == 1
        and correo.endswith(SolicitudCreditoHipotecario.__terminaciones)
        else "")