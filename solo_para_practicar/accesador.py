class Pelota():
    def __init__(self, color: str, material: str): #metodo constructor
        self.color = color
        self.material = material
    
    @property #Permite definir un método accesador
    def color_y_material(self):
        return f"Pelota {self.color} de {self.material}"

p = Pelota("Amarilla", "plástico")
# Salida: Pelota Amarilla de plástico
print(p.color_y_material)