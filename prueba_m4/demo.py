

from datetime import date
from campania import Campania
from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import Video

try:
    # Crear una instancia de Campaña con un anuncio de tipo Video
    campania = Campania("Campaña 1", date(2024, 4, 1), date(2024, 4, 30), [{"ancho": 1920, "alto": 1080, "url_archivo": "video.mp4", "url_clic": "https://www.ejemplo.com", "sub_tipo": "instream"}])

    # Solicitar un nuevo nombre de campaña
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")

    # Solicitar un nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio: ")

    # Intentar modificar el nombre de la campaña y el subtipo del anuncio
    campania.nombre = nuevo_nombre
    campania.anuncios[0].sub_tipo = nuevo_subtipo

except (LargoExcedidoError, SubTipoInvalidoError) as e:
    # Capturar excepciones y escribir el mensaje en el archivo error.log
    with open("error.log", "a") as f:
        f.write(str(e) + "\n")


""" 
from datetime import date
from campania import Campania
from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import Video

# Crear una instancia de Campaña con un anuncio de tipo Video
campania = Campania("Campaña 1", date(2024, 4, 1), date(2024, 4, 30), [{"ancho": 1920, "alto": 1080, "url_archivo": "video.mp4", "url_clic": "https://www.ejemplo.com", "sub_tipo": "instream"}])

try:
    # Solicitar un nuevo nombre de campaña
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")

    # Solicitar un nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio: ")

    # Intentar modificar el nombre de la campaña y el subtipo del anuncio
    campania.nombre = nuevo_nombre
    campania.anuncios[0].sub_tipo = nuevo_subtipo

except (LargoExcedidoError, SubTipoInvalidoError) as e:
    # Capturar excepciones y escribir el mensaje en el archivo error.log
    with open("prueba_m4/error.log", "a") as f:
        f.write(str(e) + "\n")
"""