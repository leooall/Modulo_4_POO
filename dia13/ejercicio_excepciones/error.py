from datetime import datetime
import json

instancias = []
while linea:
    try:
        producto = json.loads(linea)
        instancias.append(
            Producto(producto.get("nombre"), producto.get("precio"))
        )
        linea = productos.readline()
    except Exception as e:
















