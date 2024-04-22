#importacion de modulo 
from te import Te

#creacion de dos instancias u objeto
instancia1 = Te.precio_segun_formato()[1]
instancia2 = Te.tiempo_recomendacion()[2]

#impresion del tipo de valor de cada instancia
print(type(instancia1))
print(type(instancia2))
#comparacion de type de las instancias 
if type(instancia1) == type(instancia2):
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")     

