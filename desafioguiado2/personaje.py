#Se importa el módulo random para generar números aleatorios
import random
#Se define clase Personaje
class Personaje:
    #El método init inicializa un personaje con un nombre, nivel 1 y experiencia 0
    def __init__(self, nombre): 
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        
    #método obtener_estado devuelve una cadena que representa el estado del personaje con su nombre, nivel y experiencia.
    def obtener_estado(self): 
        return f"NOMBRE: {self.nombre}      NIVEL: {self.nivel}       EXP: {self.experiencia}"
    #método "asignar_estado" recibe un valor de experiencia y lo añade al personaje
    def asignar_estado(self, experiencia):
        if experiencia >= 0:
            self.experiencia += experiencia
            while self.experiencia >= 100:
                self.nivel += 1
                self.experiencia -= 100
        else:
            if self.nivel > 1 or self.experiencia > 0:
                self.experiencia += experiencia
                while self.experiencia < 0:
                    self.nivel -= 1
                    self.experiencia += 100
                    
    #método "probabilidad_de_ganar" calcula la probabilidad de que el personaje actual gane contra otro personaje
    #basado en la diferencia de niveles.
    def probabilidad_de_ganar(self, otro_personaje):
        if self.nivel < otro_personaje.nivel:
            return 0.33
        elif self.nivel > otro_personaje.nivel:
            return 0.66
        else:
            return 0.5

    @staticmethod
    #método estático "dialogo_enfrentamiento" imprime un mensaje, luego,
    #solicita al jugador que elija entre atacar o huir, y devuelve la opción elegida
    def dialogo_enfrentamiento(probabilidad):
        print("¡Oh no!, ¡Ha aparecido un Orco!")
        print(f"Con tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, recibirás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        opcion = input("¿Qué deseas hacer? \n1. Atacar \n2. Huir\n")
        return opcion #retorna la opcion elegida