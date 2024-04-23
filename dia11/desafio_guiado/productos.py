import json

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio
        
instancias = []
        
with open("dia11/desafio_guiado/productos.txt") as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea)
        instancias.append(Producto(producto.get("nombre"), producto.get("precio"))) 
        linea = productos.readline()

for instancia in instancias:
    print(f"{instancia.nombre} : ${instancia.precio}")
