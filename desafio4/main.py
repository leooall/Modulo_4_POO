from foto import Foto
from error import DimensionError


    
foto = Foto(4000, 2000, "rutafoto.jpg")

#Intento Foto con un ancho demasiado grande
try:
    foto.ancho = 3500  
except DimensionError as e:
    print("Error de dimension", e)

try:
    foto.alto = 3060
except DimensionError as e:
    print("Error de dimension", e)


"""
try:
    ancho = int(input("Ingrese Ancho: "))
    alto = int(input("Ingrese Alto: "))
    
    foto1 = Foto(ancho, alto, "ruta.url")
except DimensionError as e:
    print("Error de dimension", e)
"""    
