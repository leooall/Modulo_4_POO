class Pelota():
    def __init__(self):
        self.tamanio_pelota = 5
    @property
    def tamanio(self):
        return self.tamanio_pelota
    @tamanio.setter
    def tamanio(self, tamanio: int):
        self.tamanio_pelota = tamanio if tamanio > 0 else 1

p = Pelota()
print(p.tamanio)# Salida: 5 porq self.tamanio_pelota = 5

p.tamanio = 3
print(p.tamanio)# Salida: 3 porq es mayor a 0