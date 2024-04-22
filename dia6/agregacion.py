class Material():
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura
class Pelota():
    def __init__(self, tamanio: int, color: str, material: Material):
        self.tamanio = tamanio
        self.color = color
        # La pelota tiene un material
        self.material = material

# El material existe en forma independiente de la pelota
objeto_material = Material("Plástico", "Corta", "Lisa")
objeto_pelota = Pelota(16, "Amarillo", objeto_material)

print(type(objeto_pelota.material))# Salida: <class '__main__.Material'>

print(objeto_pelota.material.nombre)# Salida: Plástico
print(objeto_pelota.material.duracion)#Corta
print(objeto_pelota.material.textura)#lisa

print(objeto_material.duracion)#corta