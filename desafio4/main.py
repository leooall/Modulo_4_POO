from foto import Foto
from error import DimensionError

#creacion de un objeto de la clase Foto con argumentos
foto = Foto(2000, 2000, "rutafoto.jpg")

#Intento Foto con un ancho y alto demasiado grande
try:
    foto.ancho = 3500  
except DimensionError as e:
    print("Error de dimension", e)

try:
    foto.alto = 3060
except DimensionError as e:
    print("Error de dimension", e)

