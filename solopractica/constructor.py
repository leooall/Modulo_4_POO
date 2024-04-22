class Pelota():
    def __init__(self, color: str, tamanio: int, material: str):
        self.color = color
        self.tamanio = tamanio
        self.material = material
        
p = Pelota("Amarillo", 16, "plástico")#argumentos posicionales

print(p.color, p.tamanio, p.material)