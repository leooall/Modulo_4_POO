#POLIMORFISMO--> cambio en el comportamiento del metodo heredado desde la class padre

class Padre():
    #atributo de clase
    color = "verde"
    #constructor
    def __init__(self, tamanio: int):
        #atributos de instancia
        self.__tamanio = tamanio #atributo oculto/privado

    #metodos estaticos

    #metodos de instancia
    def cambia_color(self, color: str):
        if color != "":
            self.color = color    
    
    #sobrecarga
    def __str__(self):
        return f"El color es {self.color}, y de tamanio {self.__tamanio}"

    #getter 
    @property
    def tamanio(self):
        return self.__tamanio
    
    # setters
    @tamanio.setter
    def tamanio(self, tamanio: int):
        if tamanio > 0:
            self.__tamanio = tamanio
        else:
            self.__tamanio = 0
        
#HERENCIA --> hereda todoooo  y cada uno de los hijos puede tener sus propios metodos y atributos  
class Hija(Padre):
    peso = 100
    
    #POLIMORFISMO--> cambio en el comportamiento del metodo heredado del padre
    def cambia_color(self, color: str):
        self.color = color 
############################################################################################
class Hijo(Padre):
    deuda = 120
    #sobrescribir el constructor
    def __init__(self, tamanio: int, saldo = 0):
        super().__init__(tamanio)#llamado al constructor del padre
        self.__saldo = saldo
    @property #getter 
    def saldo(self):
        return self.__saldo
#############################################################################################    
class Nieto(Hija): #hereda de la mamá el peso, y del abuelo el color y tamanio
    pañal = "xl"


#instancia de la clase hija (creando un objeto)
hijita = Hija(100)
hijita.cambia_color("rosa")
print(f"el color de la class hija es {hijita.color}")#el color de la class hija es rosa
print(f"el tamanio de la class hija es {hijita.tamanio}")#el tamanio de la class hija es 100

regalon = Nieto(50)
regalon.cambia_color("azul")

print(f"el color de la class nieto es {regalon.color}")#el color de la class nieto es azul
print(f"el tamanio de la class nieto es {regalon.tamanio}")#el tamanio de la class nieto es 50

#la herencia es unidireccional y un subclass no puede añadirle metodos ni atributos al Padre

super(type(hijita),hijita).cambia_color("gris")
print(f"el color de la clase hija es {hijita.color}")

hijito = Hijo(10, 1200)
print(hijito.tamanio, hijito.saldo, hijito.deuda)

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"hijita es intancia de Hija: {isinstance(hijita,Hija)}")#True
print(f"hijita es intancia de hijo: {isinstance(hijita,Hijo)}")#False
print(f"hijita es intancia de padre: {isinstance(hijita,Padre)}")#True
print(f"hijita es intancia de nieto: {isinstance(hijita,Nieto)}")#False