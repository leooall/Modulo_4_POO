"""class MisExcepciones(Exception):
    
    def imprimir_promedio(self, dividendo, divisor):
        promedio = dividendo/divisor #ZeroDivisionError: division by zero
        print(f"el promedio es {promedio}")
        
calculo_promedio = MisExcepciones()
calculo_promedio.imprimir_promedio(100, 0)
"""

##################################
class Error(Exception):
    pass
class DivisorError(Error):
    def __init__(self, mensaje, divisor: int):
        self.divisor = divisor
        self.mensaje = mensaje

class MisExcepciones(Exception):
    
    def imprimir_promedio(self, dividendo, divisor):
        try:
            promedio = dividendo/divisor 
            print(f"el promedio es {promedio}")
        except ZeroDivisionError:
            print("el divisor no puede ser un cero")
        #captura generica de una excepcion
        except Exception as error:
            print("se ha producido un error", error) #se ha producido un error division by zero
        finally: #SIEMPRE SE EJECUTARA: OJO CON LO QUE COLOQUEMOS
            print("el metodo se ha ejecutado")

calculo_promedio = MisExcepciones()

valido = True
while valido:
    try: 
        dividendo = int(input("ingrese el numero dividendo > "))
        valido = False
    except ValueError:
        print("error, debe ingresar un numero")
        
valido = True        
while valido:   
    try: 
        divisor = int(input("ingrese el numero divisor > "))
        if divisor == 0:
            raise DivisorError("divisor no puede ser ceroo", divisor)
        valido = False
    except DivisorError as de:
        print("Error en el ingreso del divisorr", de)
    except ValueError:
        print("Error, debe ingresar un numero")
    
calculo_promedio.imprimir_promedio(dividendo,divisor)