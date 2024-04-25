import json

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio
        
instancias = []
        
with open("dia11/desafio_guiado/productos.txt") as productos:
    linea = productos.readline()
    while linea:
        try:
            producto = json.loads(linea)
            instancias.append(Producto(producto.get("nombre"), producto.get("precio"))) 
            linea = productos.readline()
        except Exception as e:
            with open("error.log", "a+") as log:
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}]"
                f" ERROR: {e}\n")
        finally:
            linea = productos.readline()


for instancia in instancias:
    print(f"{instancia.nombre} : ${instancia.precio}")
