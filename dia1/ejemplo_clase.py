#def de la class
class Pelota():  #siempre la clase es con la primera letra mayuscula
    #atributos
    forma = "redonda"
    
#instancia de la clase => creacion un objeto a partir de una clase
pelota_de_andy = Pelota()
print(pelota_de_andy.forma) #el .forma es el atributo heredado

#definicion de clase
class Medicamento():
    descuento = 0.05
    IVA = 0.18