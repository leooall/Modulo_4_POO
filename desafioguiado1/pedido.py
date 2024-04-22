#importacion de modulo te y su class Te
from te import Te

#mensaje de bienvenida
print("Bienvenido")

#integracion de la eleccion de te y su formato en variables distintas, ambas transformadas a int
eleccion_de_te = int(input("¿Que preferencia de Té desea? 1: Corresponde a Té negro, 2: Corresponde a Té verde, 3: Corresponde a Agua de hierbas\n>"))
eleccion_de_formato = int(input("Elija un formato. 1: 300gr, 2: 500gr\n>"))

# eleccion te negro y sus formatos
if eleccion_de_te == 1 and eleccion_de_formato == 1:
    print(F"Su sabor de Té seleccionado es : {Te.sabores[0]} \nFormato de : {Te.formatos[0]} gr \nEl precio es de : {Te.precio_segun_formato()[0]} pesos \nTiempo de expiracion es {Te.expiracion} días \nRecomendacion : {Te.tiempo_recomendacion()[0]}")
elif eleccion_de_te == 1 and eleccion_de_formato == 2:
    print(F"Su sabor de Té seleccionado es : {Te.sabores[0]} \nFormato de : {Te.formatos[1]} gr \nEl precio es de : {Te.precio_segun_formato()[1]} pesos \nTiempo de expiracion es {Te.expiracion} días \nRecomendacion : {Te.tiempo_recomendacion()[0]}")

# eleccion te verde y sus formatos
elif eleccion_de_te == 2 and eleccion_de_formato == 1:
    print(F"Su sabor de Té seleccionado es : {Te.sabores[1]} \nFormato de : {Te.formatos[0]} gr \nEl precio es de : {Te.precio_segun_formato()[0]} pesos \nTiempo de expiracion es {Te.expiracion} días \nRecomendacion : {Te.tiempo_recomendacion()[1]}")
elif eleccion_de_te == 2 and eleccion_de_formato == 2:
    print(F"Su sabor de Té seleccionado es : {Te.sabores[1]} \nFormato de : {Te.formatos[1]} gr \nEl precio es de : {Te.precio_segun_formato()[1]} pesos \nTiempo de expiracion es {Te.expiracion} días \nRecomendacion : {Te.tiempo_recomendacion()[1]}")

# eleccion infusion de hierbas y sus formatos
elif eleccion_de_te == 3 and eleccion_de_formato == 1:
    print(F"Su sabor de Té seleccionado es : {Te.sabores[2]} \nFormato de : {Te.formatos[0]} gr \nEl precio es de : {Te.precio_segun_formato()[0]} pesos \nTiempo de expiracion es {Te.expiracion} días \nRecomendacion : {Te.tiempo_recomendacion()[2]}")
elif eleccion_de_te == 3 and eleccion_de_formato == 2:
    print(F"Su sabor de Té seleccionado es : {Te.sabores[2]} \nFormato de : {Te.formatos[1]} gr \nEl precio es de : {Te.precio_segun_formato()[1]} pesos \nTiempo de expiracion es {Te.expiracion} días \nRecomendacion : {Te.tiempo_recomendacion()[2]}")

#mensaje de error si no se cumple ninguna condicion anterior
else:
    print("Por favor ingrese numeros validos, vuelva a intentarlo")    