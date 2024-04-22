from abc import ABC, abstractmethod #se importa abc para crear una clase abstracta

class Pelota(ABC):
    #definicion del metodo ABSTRACTO, no tiene implementacion
    @abstractmethod
    def rebotar(self, altura: int):
        pass
    

#pelotita = Pelota()#no se puede instanciar una clase abstracta
#TypeError: Can't instantiate abstract class Pelota without an implementation for abstract method 'rebotar'

class PelotaDeJuguete(Pelota):
    def __init__(self, color: str):
        self.rebotes=[]
        #__ para definir atributo privado
        self.__color = color

    #ES OBLIGATORIO implementar el metodo que es abstracto
    def rebotar(self, altura: int):
        print(altura)
        
    #metodo get --> traer informacion de un atributo
    @property
    def color(self):
        return self.__color
    
    #metodo set --> asigna valor al atributo
    @color.setter
    def color(self,nuevo_color: str):
        self.__color = nuevo_color
    
    
pelotita =  PelotaDeJuguete("amarilla")
print("llamado al get de color", pelotita.color)

#pelotita.color("azul") -->no se deb tratar como metodo, sino como atributo
pelotita.color = "azul" #---> tratar setter como atributo
print("llamado al get de color", pelotita.color) #gett






