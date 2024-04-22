#Se importa la clase "Personaje" del archivo "personaje.py"
#Se importa el módulo "random" para generar números aleatorios
from personaje import Personaje
import random

#Se define la clase "Juego" con un constructor pero sin atributos
class Juego:
    def __init__(self):
        pass
    
    #definicion del metodo "jugar"
    def jugar(self):
        print("¡Bienvenido a Gran Fantasía!")
        nombre_personaje = input("Por favor, indique el nombre de su personaje: ")
        #Se crea un objeto "jugador" de la clase "Personaje" con el nombre proporcionado por el usuario.
        jugador = Personaje(nombre_personaje)
        print(jugador.obtener_estado())#Se imprime el estado del jugador
        #Se crea un objeto "orco" de la clase "Personaje" con el nombre "Orco"
        orco = Personaje("Orco")
        #Se calcula la probabilidad de ganar del jugador contra el orco, segun diferencia de niveles
        probabilidad = jugador.probabilidad_de_ganar(orco)
        opcion = Personaje.dialogo_enfrentamiento(probabilidad)

        while opcion == "1": #Mientras el usuario elija atacar
            resultado_ataque = random.uniform(0, 1) #Se genera un resultado de ataque aleatorio
            if resultado_ataque <= probabilidad: #Si el resultado de ataque es menor o igual a la probabilidad de ganar, el jugador gana
                print("¡Le has ganado al orco, felicidades!")
                print("¡Recibirás 50 puntos de experiencia!")
                jugador.asignar_estado(50) # se le asigna al jugador 50 puntos de experiencia
                orco.asignar_estado(-30) # se le resta30pts al orco de experiencia
            else:#Si el resultado de ataque es mayor a la probabilidad de ganar, el jugador pierde
                print("¡Oh no! ¡El orco te ha ganado!")
                print("¡Has perdido 30 puntos de experiencia!")
                jugador.asignar_estado(-30) # se le resta 30pts al jugador de experiencia
                orco.asignar_estado(50) # se le asigna al orco 50pts de experiencia
            print(jugador.obtener_estado()) # impresionn estado jugador
            print(orco.obtener_estado()) #impresion estado orco
            probabilidad = jugador.probabilidad_de_ganar(orco) #Se calcula la probabilidad de ganar del jugador contra el orco, segun diferencia de niveles
            opcion = Personaje.dialogo_enfrentamiento(probabilidad) #dialogo y solicitud de eleccion 1 o 2

        if opcion == "2":
            print("¡Has huido! El orco ha quedado atrás.")

#verificacion de que este script es el de ejecucion principal
if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
