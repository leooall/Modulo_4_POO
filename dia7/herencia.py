#la idea de la herencia es reutilizar los metodos y atributos en las herencias hijas
class Padre():
    
    def __init__(self, color: str):
        self.__color = color #atributo oculto
        
    @property
    def color(self) -> str:
        return self.__color
    
    def imprimir(self):
        print("este metodo pertenece a la clase padre")
################################################################
#la class hija hereda los atributos y metodos de la class padre
class Hija(Padre):
    def mostrar_color(self):
        print(f"Mi color es {self.color}")
############################################################        
pdf = Hija("Blanco y Negro")

pdf.mostrar_color()# Salida: Mi color es Blanco y Negro

papa = Padre("Azul y Blanco")
print(papa.color)  #Salida: Azul y Blanco



hijita =Hija("rojo y cafe")
hijita.mostrar_color()
print(hijita.color)
hijita.imprimir()
#########################################################
class Nieta(Hija):
    def imprimir_nieta(self):
        print("este metodo pertenece a la clase")




