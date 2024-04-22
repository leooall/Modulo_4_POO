class Madre():
    def __init__(self, color: str, **kwards):
        super().__init__(**kwards)
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
        
#############################################
class Padre():
    def __init__(self, tamanio: int, **kwards):
        super().__init__(**kwards)
        self.__tamanio = tamanio

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        self.__tamanio = tamanio
        
############################################       
class Hija(Madre, Padre):
    """sobrescritura de los constructores"""    
    #def __init__(self, color: str, tamanio: int):
    #    Madre.__init__(self, color)
    #    Padre.__init__(self, tamanio)
    """otra forma de sobrescritura de los constructores"""
    def __init__(self, deuda = 0, **kwards):
        super().__init__(**kwards)
        
        #atributo de instancia propio de hija
        self.deuda = deuda
        
#objeto
#princesa = Hija("rojo", 80)
princesa = Hija(deuda = 1000000, color = "rojo", tamanio = 80)

#si los atributos se repiten en las clases superiores se le asigna a la primera clase de izq a dere 
print(princesa.color, princesa.tamanio, princesa.deuda)

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"princesa es intancia de Hija: {isinstance(princesa,Hija)}")#True
print(f"princesa es intancia de Padre: {isinstance(princesa,Padre)}")#True
print(f"princesa es intancia de Madre: {isinstance(princesa,Madre)}")#True
        
        
        
        
        
        
        
        
        