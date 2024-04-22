from pelota import Pelota

#instancia de clase o creacion del objeto
pelota_futbol = Pelota("amarillo",14, "cuero")#argumentos possicionales

print(pelota_futbol.color, pelota_futbol.material, pelota_futbol.tamanio)
print(pelota_futbol.forma)

print("*********")
#instancia de clase, con valor por defecto
pelota_basket = Pelota("naranjo",None, "caucho")#argumentos posicionales 

#atributo de clase
print(pelota_basket.forma)
pelota_basket.tamanio = 8 #se cambia none por un valor numerico
print(pelota_basket.tamanio)
print(pelota_basket.color)

print(Pelota.forma) #directo con la clase solo tengo acceso a la forma

print(pelota_futbol.color_y_material)
#accesador del atributo (get)
print("con property",pelota_futbol.colores)
print("metodo get",pelota_futbol.getColor())

#mutadores 
#por default
pelota_futbol.color = "Negro"
print("por default",pelota_futbol.color)

#a traves de metodo
pelota_futbol.setColor("Roja")
print("con metodo",pelota_futbol.color)

#a traves de setter
pelota_futbol.colores = ""
print("con setter",pelota_futbol.color)
()
print(pelota_futbol)