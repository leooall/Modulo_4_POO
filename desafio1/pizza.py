from ingredientes import vegetales, proteicos, masas
#definicion de la clase
class Pizza:
    #atributos
    vegetales = []
    proteicos = []
    masas = []
    precio = 10000
    tamaño = "familiar"
    
    #metodo estatico
    @staticmethod
    #Valida cada elemento ingresado en una lista de posibles_valores
    def validar_elemento(elemento, posibles_valores): 
        return elemento in posibles_valores
    
    #metodo NO estatico
    def realizar_pedido(self):
        
        #agrega el valor de input a la lista del atributo proteicos
        self.proteicos = input("""Escriba la proteína a elegir:
            pollo, vacuno, carne vegetal: 
            """)
        #valida el valor ingresado en input con la lista de proteicos del script ingredientes.py 
        val_pro = self.validar_elemento(self.proteicos, proteicos)
        
        self.vegetales = []
        vegetal1 = input("""Escriba su primer vegetal: 
                            tomate, aceitunas, champiñones: """)
        self.vegetales.append(vegetal1)#agrega vegetal1 a la lista del atributo vegetales
        
        #valida el valor ingresado en input con la lista de vegetales del script ingredientes.py
        #ademas guarda el parametro en una variable 
        val_veg1 = self.validar_elemento(vegetal1, vegetales)
        
        #agrega directamente el input a la lista del atributo vegetales
        self.vegetales.append(input("""Escriba su segundo vegetal: 
                                    tomate, aceitunas, champiñones: """))
        
        #valida el valor ingresado en input con la lista de vegetales del script ingredientes.py
        #ademas guarda el parametro en una variable 
        val_veg2 = self.validar_elemento(vegetales[1], vegetales)
        
        #agrega directamente el input a la lista del atributo masas
        self.masas = input("ingrese la masa a elegir; tradicional o delgada ")
        
        #valida el valor ingresado en input con la lista de masas del script ingredientes.py
        val_masa = self.validar_elemento(self.masas,masas)
        
        #validacion de pizza
        self.pizza_valida = val_pro and val_veg1 and val_veg2 and self.validar_elemento(self.masas,masas)        
        

#verifica si el atributo pizza_valida de la instancia pizza1 de la clase Pizza es verdadero.
if __name__ == "__main__":
    pizza1 = Pizza()
    pizza1.realizar_pedido()
    if pizza1.pizza_valida:
        print("la pizza es valida")