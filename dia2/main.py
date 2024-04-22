from pelota import Pelota

pelota_multicolor = Pelota()

#print(pelota_multicolor.color)#AttributeError: 'Pelota' object has no attribute 'color'

#inicializar un atributo de instancia con valor inicial
pelota_multicolor.inicia_color()#El color de esta pelota es 

# Se asigna color a la instancia
pelota_multicolor.asigna_color("rojo")#<pelota.Pelota object at 0x00000245CBCB5EB0> <class 'pelota.Pelota'>
print(pelota_multicolor.color)#rojo


pelota_multicolor.lee_color()#"El color de esta pelota es rojo"
pelota_multicolor.asigna_color("verde")#<pelota.Pelota object at 0x00000245CBCB5EB0> <class 'pelota.Pelota'>

pelota_multicolor.lee_color_local_y_atributo("amarillo")#El color amarillo NO es el color de ESTA pelota